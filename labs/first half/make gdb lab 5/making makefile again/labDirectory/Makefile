.PHONY: restore

CXX = g++
CXXFLAGS = -Wall -Wextra -std=c++11

non_main = hehe.cpp haha.cpp nohehe.cpp
main = powerful.cpp restore.cpp

obj = $(patsubst %.cpp,%.o,$(non_main))
executables = powerful restored

all: $(obj) $(executables)

hehe.o: hehe.cpp card.h
	$(CXX) $(CXXFLAGS) -c $< -o $@

haha.o: haha.cpp player.h card.h
	$(CXX) $(CXXFLAGS) -c $< -o $@

nohehe.o: nohehe.cpp deck.h card.h
	$(CXX) $(CXXFLAGS) -c $< -o $@

powerful: powerful.cpp hehe.o
	$(CXX) $(CXXFLAGS) $^ -o powerful

restored: restore.cpp nohehe.o haha.o hehe.o
	$(CXX) $(CXXFLAGS) $^ -o restore

restore:
	rm -f $(obj) restore powerful
