program summation
implicit none
integer :: sum, a, nums
print*, "This program performs 5 summations"
sum = 0
nums = 0
do
print*, "Add:"
read*, a
if (nums == 4) then
sum = sum + a
exit
else
    nums= nums + 1
sum = sum + a
end if
end do
print*, "Summation =", sum
end
