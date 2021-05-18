cmake_minimum_required(VERSION 3.5.1)
project(mygamestatic)
link_directories(~/usr/local/lib )
set(PROJECT_LINK_LIBS libMyEngineStatic.a)

include_directories(~/usr/local/include)
add_executable(mygamestatic mygame.cpp)
target_link_libraries(mygamestatic ${PROJECT_LINK_LIBS})

project(mygamedynamic)
link_directories(~/usr/local/lib )
set(PROJECT_LINK_LIBS libMyEngineDynamic.so)

include_directories(~/usr/local/include)
add_executable(mygamedynamic mygame.cpp)
target_link_libraries(mygamedynamic ${PROJECT_LINK_LIBS})
