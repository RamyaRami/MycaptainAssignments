"""python program to accept a filename from a user and print
theextension of that"""


a=input("enter a filename")
ext=a.split(".")
print("fle extension:",(ext[-1]))
