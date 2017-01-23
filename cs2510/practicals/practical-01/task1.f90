! sum.f90
! Performs summations using in a loop using EXIT statement
program summation
implicit none
integer :: sum, a
print*, "This program counts the number of inputs. input 0 to exit."
sum = 0
do
print*, "Add:"
read*, a
if (a == 0) then
exit
else
sum = sum + 1
end if
end do
print*, "Summation =", sum
end
