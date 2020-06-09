cmake_minimum_required(VERSION 3.0.2)
project(lang_process) #패키지명

#없으면 빌드시 설치하라고 메세지 
find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  roscpp
  rospy
  std_msgs
)


catkin_package(
#  INCLUDE_DIRS includes
   LIBRARIES lang_process #라이브러리 = 패키지 이름
   CATKIN_DEPENDS geometry_msgs roscpp rospy std_msgs 
#  DEPENDS system_lib
)

# 3개의 노드(실행파일) 필요. 그런데 cpp은 하나 뿐이라 add_executable 하나만해도되나?
include_directories(${catkin_INCLUDE_DIRS})
add_executable(lang_process src/lang_process_node.cpp)
add_dependencies(${PROJECT_NAME}_node ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS}) #의존성 있는 빌드 옵션들 수행 가능




