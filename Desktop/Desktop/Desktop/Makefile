OBJS	= cApp.o cMain.o
SOURCE	= cApp.cpp cMain.cpp
HEADER	= cApp.h cMain.h
OUT	= a.out
CC	 = g++
FLAGS	= -g -c -Wall `wx-config --cxxflags` `wx-config --libs`
LFLAGS	 = 

all: $(OBJS)
	$(CC) -g $(OBJS) -o $(OUT) $(LFLAGS)

TESTTApp.o: TESTTApp.cpp
	$(CC) $(FLAGS) TESTTApp.cpp 

TESTTMain.o: TESTTMain.cpp
	$(CC) $(FLAGS) TESTTMain.cpp 


clean:
	rm -f $(OBJS) $(OUT)

run: $(OUT)
	./$(OUT)