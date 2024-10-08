cmake_minimum_required(VERSION 3.12)

project(yolov8-detect)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++17 -O3")


list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/cmake")
include(Function)

# CUDA
find_package(CUDA REQUIRED)
print_var(CUDA_LIBRARIES)
print_var(CUDA_INCLUDE_DIRS)
get_filename_component(CUDA_LIB_DIR ${CUDA_LIBRARIES} DIRECTORY)
print_var(CUDA_LIB_DIR)

# OpenCV
set(CMAKE_PREFIX_PATH "F:/ThirdPart/OpenCV" ${CMAKE_PREFIX_PATH})
find_package(OpenCV REQUIRED)
print_var(OpenCV_LIBS)
print_var(OpenCV_LIBRARIES)
print_var(OpenCV_INCLUDE_DIRS)

# TensorRT
list(APPEND CMAKE_PREFIX_PATH "F:/ThirdPart/TensorRT-8.4.3.1" ${CMAKE_PREFIX_PATH})
find_package(TensorRT REQUIRED)
print_var(TensorRT_LIBRARIES)
print_var(TensorRT_INCLUDE_DIRS)
print_var(TensorRT_LIB_DIR)
if (TensorRT_VERSION_MAJOR GREATER_EQUAL 10)
    message(STATUS "Build with -DTRT_10")
    add_definitions(-DTRT_10)
endif ()

list(APPEND ALL_INCLUDE_DIRS
        ${CUDA_INCLUDE_DIRS}
        ${OpenCV_INCLUDE_DIRS}
        ${TensorRT_INCLUDE_DIRS}
        ${CMAKE_CURRENT_SOURCE_DIR}/include
)

list(APPEND ALL_LIBS
        ${CUDA_LIBRARIES}
        ${OpenCV_LIBRARIES}
        ${TensorRT_LIBRARIES}
)

list(APPEND ALL_LIB_DIRS
        ${CUDA_LIB_DIR}
        ${TensorRT_LIB_DIR}
)

print_var(ALL_INCLUDE_DIRS)
print_var(ALL_LIBS)
print_var(ALL_LIB_DIRS)


add_executable(
        ${PROJECT_NAME}
        ${CMAKE_CURRENT_SOURCE_DIR}/main.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/src/yolov8.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/src/detect_service.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/include/common.hpp
)

add_executable(
        test
        ${CMAKE_CURRENT_SOURCE_DIR}/test.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/src/yolov8.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/src/detect_service.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/include/common.hpp
)

target_include_directories(
        ${PROJECT_NAME}
        PUBLIC
        ${ALL_INCLUDE_DIRS}
)

target_link_directories(
        ${PROJECT_NAME}
        PUBLIC
        ${ALL_LIB_DIRS}
)

target_link_libraries(
        ${PROJECT_NAME}
        PRIVATE
        ${ALL_LIBS}
)
# ---------------------------------------
target_include_directories(
        test
        PUBLIC
        ${ALL_INCLUDE_DIRS}
)

target_link_directories(
        test
        PUBLIC
        ${ALL_LIB_DIRS}
)

target_link_libraries(
        test
        PRIVATE
        ${ALL_LIBS}
)

if (${OpenCV_VERSION} VERSION_GREATER_EQUAL 4.7.0)
    message(STATUS "Build with -DBATCHED_NMS")
    add_definitions(-DBATCHED_NMS)
endif ()
