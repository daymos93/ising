program Ising
    use ziggurat !es modulo de fortran (coleccion de rutinas o variables)
    implicit none !nada implicito, defino todas las variables
    logical :: es !definicion de variable logica (type::var_name)
    integer :: seed,i ,j, k, pmc, S(0:21,0:21),flip_x, flip_y, N, acc
    real(kind=8):: JJ,E_ini,E,E0,E1,dE,aux_1,aux_2,T,m_ini,m,ratio,Ec,Ec2,Mc,Mc2,Emean,Mmean,Eerror,Merror,Evar,Mvar,pmcr

!T = 300 !!Temperatura del sistema (lo ingreso desde imput.dat)
JJ = 1
N = 20 !!Elementos de la matriz
!pmc = 1000 !pasos de Monte Carlo (lo ingreso desde imput.dat)
acc = 0

!!!!!!!!!!!!!!!!!!!!! Leo del input cantidad de pasos de MC (pmc) y temperatura del run !!!!!!!!!!!!!!!!

        open(unit = 10, file = 'input.dat', status = 'old')
        read(10,*)
        read(10,*) T, pmc
        close(10)

print*, "  ************** Modelo Ising @ T =",T,"**************" 

![NO TOCAR] Inicializa generador de número random

    inquire(file='seed.dat',exist=es)!pregunta al SO si seed.dat existe y guarda la rta logica en es
    if(es) then
        open(unit=10,file='seed.dat',status='old')
        read(10,*) seed
        close(10)
        print *,"  * Leyendo semilla de archivo seed.dat"
    else
        seed = 24583490
    end if

    call zigset(seed)

![FIN NO TOCAR]   



!!!!!!!!!! Verifico si existe o genero matriz inicial\

    inquire(file='matrix.dat',exist=es)!pregunta al SO si matrix.dat existe y guarda la rta logica en es
    if(es) then
        open(unit=10,file='matrix.dat',status='old')
        read(10,*) S
        close(10)
        print*, "  * Usando matriz OLD" 
     else
        do i=1,20
                do j=1,20
                        aux_1=uni()
                        if(aux_1 .le. 0.5) then
                                S(i,j)=-1
                        else
                                S(i,j)=1
                        end if 
                end do
        end do

     S(:,21)=S(:,1)
     S(:,0)=S(:,20)
     S(21,:)=S(1,:)
     S(0,:)=S(20,:)
      
     print*, "  * Usando matriz NEW"

     end if


!!!!!!!! Calculo energia inicial a 1eros vecinos

E_ini=0
m_ini=0 

do i=1,20
        do j=1,20
                E_ini=E_ini-JJ*S(i,j)*(S(i-1,j)+S(i,j-1)) !Energia inicial
                m_ini=m_ini+S(i,j) !magnetizacion inicial
        end do
end do

E = E_ini
m = m_ini

 Ec = E
 Ec2 = E**2
 Mc = m
 Mc2 = m**2
 

print*, "    E_inicial", E,"M_inicial",m_ini



!!!!!!!!!!!!!!!!!!!!! abro el archivo de salida !!!!!!!!!!!!!!!!
open(unit = 10, file = 'output.dat', status = 'unknown')
write(10,*) 'Temperature',T
!write(10,*) "Energy","    ","Magnetization"
open(unit = 1, file = 'hist.dat', status = 'unknown')


!!!!!!!!!!!!!!!!!!!!!!!!!!!! Sorteo de spin (Metropolis) !!!!!!!!!!!!!!!!!!!!!!!!!

do k=1,pmc
        flip_x=int(uni()*20+1);flip_y=int(uni()*20+1)

        E0 = -JJ*S(flip_x,flip_y)*(S(flip_x-1,flip_y)+S(flip_x+1,flip_y)+S(flip_x,flip_y-1)+S(flip_x,flip_y+1))
        S(flip_x,flip_y) = -1*S(flip_x,flip_y)
        E1 = -JJ*S(flip_x,flip_y)*(S(flip_x-1,flip_y)+S(flip_x+1,flip_y)+S(flip_x,flip_y-1)+S(flip_x,flip_y+1))
        dE = E1-E0

        if (uni() > exp(-dE/T)) then 					!Rechazo el flip
                S(flip_x,flip_y) = -1*S(flip_x,flip_y)
                
        else 											!Acepto el flip
                E = E + dE
                m = m + 2*S(flip_x,flip_y)
                acc = acc + 1

			     S(:,21)=S(:,1)
    			 S(:,0)=S(:,20)
   				  S(21,:)=S(1,:)
    			 S(0,:)=S(20,:)        
        end if
        write(1,*) E,m
		Ec = Ec + E
        Mc = Mc + m
        Ec2 = Ec2 + E**2
        Mc2 = Mc2 + m**2

        !if (mod(k,1000)==0) then 
                !print*, k, E, m
                !write(10,*) E, m
        !end if
!print*,acc
end do

pmcr = real(pmc,kind=8)

ratio = real(acc,kind=8)/pmcr*100 !ratio de acceptación

Emean = Ec/pmcr
Mmean = Mc/pmcr
Evar = Ec2/pmcr - Emean**2
Mvar = Mc2/pmcr - Mmean**2
Eerror = sqrt(Evar/pmcr)
Merror = sqrt(Mvar/pmcr)


!print*,acc,pmc,ratio,Eerror,Merror
write(10,*) "Mean energy", Emean
write(10,*) "Evar", Evar
write(10,*) "Eerror", Eerror


write(10,*) "Mean magnetization", Mmean
write(10,*) "Mvar", Mvar
write(10,*) "Merror", Merror


write(10,*) "Ratio", ratio
close(10)
close(1)

print*, "    E_final", E,"M_final",m

!!escribir la ultima matriz para iniciar desde aqui

        open(unit=10,file='matrix.dat',status='unknown') 
        !do i=0,21
        write(10,*) S
        !end do
        !write( 10 , "(*(g0))" ) ( (S(i,j)," ",j=0,21), new_line("A"), i=0,21 )
        close(10)


print*, "  ************** END **************"


!! 
!! FIN FIN edicion
!! 
![No TOCAR]
! Escribir la última semilla para continuar con la cadena de numeros aleatorios 

        open(unit=10,file='seed.dat',status='unknown')
        seed = shr3() 
        write(10,*) seed
        close(10)

![FIN no Tocar]        


end program Ising
