.PHONY: all clean
CXX := g++
CXXFLAGS := -Wall -std=c++17
srcs1 := $(wildcard ./src/src1/*.cpp)
srcs2 := $(wildcard ./src/src2/*.cpp)
obj1 := $(patsubst ./src/src1/%.cpp, %.o, $(srcs1))
obj2 := $(patsubst ./src/src2/%.cpp, %.o, $(srcs2))
MAINFILES := $(basename $(notdir $(wildcard ./main/main[0-9].cpp)))
dirr := $(shell pwd)

all: $(obj1) $(obj2) $(MAINFILES)

%.o : ./src/src1/%.cpp ./src/src1/%.h
	$(CXX) $(CXXFLAGS) -c $< -o $@

%.o : ./src/src2/%.cpp ./src/src2/%.h
	$(CXX) $(CXXFLAGS) -c $< -o $@

main% : $(obj1) $(obj2) ./main/main%.cpp 
	$(CXX) $(CXXFLAGS) $^ -o $@

clean:
	rm -f $(obj1) $(obj2) $(MAINFILES)