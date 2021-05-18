cmake_minimum_required(VERSION 3.5.1)
project (helloworld)
add_executable(helloworld helloworld.cpp)


project (usespthread)
set(THREADS_PREFER_PTHREAD_FLAG ON)
find_package(Threads REQUIRED)
add_executable(usespthread usespthread.cpp )
target_link_libraries (usespthread Threads::Threads)


project (MyEngineDynamic)
set(CMAKE_BUILD_TYPE Release)
include_directories(myengine/myengine.hpp)
set(SOURCE1 myengine/myengine.cpp)
add_library(MyEngineDynamic SHARED ${SOURCE1})

project (MyEngineStatic)
set(CMAKE_BUILD_TYPE Release)
include_directories(myengine/myengine.hpp)
set(SOURCE2 myengine/myengine.cpp)
add_library(MyEngineStatic STATIC ${SOURCE1})

install(FILES myengine/myengine.hpp DESTINATION /usr/local/include)
install(TARGETS MyEngineDynamic DESTINATION /usr/local/lib )
install(TARGETS MyEngineStatic DESTINATION /usr/local/lib )

