#.DEFAULT_GOAL := generate #choose the default goal instead of it being the first one
.PHONY: clean #tells make that these goals are not files but some other thing

# Compiler path
UNAME_S := $(shell uname -s)
ifeq ($(UNAME_S),Darwin)
	compPath = /usr/local/bin/g++-11
else
	compPath := $(shell which g++)
endif

# Compiler options, debug and performance
cppDebugFlags = -std=c++17 \
				-Wall \
				-Wextra \
				-Wpedantic \
				-g \
				-O0
cppPerfFlags = -std=c++17 -O3
OMP_FLAG = -fopenmp
# cppFlags = ${cppDebugFlags} #the version used
cppFlags = ${cppPerfFlags} #the version used


# Make a list of all the source files that end in .cpp
SRCS = $(wildcard src/*.cpp)

# Make a list of all object files. This can be automatically expanded
OBJS = $(SRCS:.c=.o)

# what is require goes first. After the colon are the required items. Then what
# to do is indented
# $@ is an automatic variable that is the target name
rw-main.exe : $(OBJS)
	$(compPath) $(cppFlags) $(OMP_FLAG) $(OBJS) -o  bin/$@
	@echo "Build Complete"

# Create all object files.
%.o: %.cpp
	$(compPath) $(cppFlags) $(OMP_FLAG) -c $< -o $@

clean:
	@echo "Cleaning up..."
	@rm -rf bin/*.exe*
	@rm -f src/*.mod
	@rm -f src/*.o
	@rm -rf doxygen-html
	@echo "Done"
