OBJS = main.o depend.o
CC = g++
CFLAGS = -Wall -c
LFLAGS = -Wall

all : $(OBJS)
	$(CC) $(LFLAGS) $(OBJS) -o main

main.o : main.cpp depend.h
	$(CC) $(CFLAGS) main.cpp

depend.o : depend.cpp depend.h
	$(CC) $(CFLAGS) depend.cpp

.PHONY: Clean
Clean : 
	\rm *.o main

.PHONY: skiprebuild
skiprebuild :
	touch -m main.o depend.o depend.h

.PHONY: skiprebuildh
skiprebuildh :
	touch -r depend.o depend.h
	touch -r main.o depend.h