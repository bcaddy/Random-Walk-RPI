#.DEFAULT_GOAL := generate #choose the default goal instead of it being the first one
.PHONY: clean #tells make that these goals are not files but some other thing

# compiler options, debug and performance
cppDebug = g++ \
           -std=c++17 \
		   -Wall \
		   -Wextra \
		   -Wpedantic \
		   -g \
		   -O0
cppPerf = g++ -std=c++17 -O3
cppCompiler = ${cppDebug} #the version used


# Make a list of all the source files that end in .cpp
SRCS = $(wildcard src/*.cpp)

# Make a list of all object files. This can be automatically expanded
OBJS = $(SRCS:.c=.o)

# what is require goes first. After the colon are the required items. Then what
# to do is indented
# $@ is an automatic variable that is the target name
rw-main.exe : $(OBJS)
	$(cppCompiler) $(OBJS) -o  bin/$@
	@echo "Build Complete"

# Create all object files.
%.o: %.cpp
	$(cppCompiler) -c $< -o $@

clean:
	@echo "Cleaning up..."
	@rm -rf bin/*.exe*
	@rm -f src/*.mod
	@rm -f src/*.o
	@rm -rf doxygen-html
	@echo "Done"
