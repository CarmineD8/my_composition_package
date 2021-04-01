cmake_minimum_required(VERSION 3.5)
project(my_composition_package)

# Default to C99
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
find_package(rclcpp_components REQUIRED)
find_package(example_interfaces REQUIRED)

add_library(talker_component SHARED
  src/publisher.cpp)
  
add_library(listener_component SHARED
  src/subscriber.cpp)

add_library(client_component SHARED
  src/client.cpp)  

add_library(server_component SHARED
  src/server.cpp)  
   

rclcpp_components_register_node(talker_component
  PLUGIN "my_composition_package::MinimalPublisher"
  EXECUTABLE comp_publisher)
  
rclcpp_components_register_node(listener_component
  PLUGIN "my_composition_package::MinimalSubscriber"
  EXECUTABLE comp_subscriber)

rclcpp_components_register_node(client_component
  PLUGIN "my_composition_package::MinimalClient"
  EXECUTABLE comp_client)
  
rclcpp_components_register_node(server_component
  PLUGIN "my_composition_package::MinimalServer"
  EXECUTABLE comp_server)
  
ament_target_dependencies(talker_component rclcpp rclcpp_components std_msgs)
ament_target_dependencies(listener_component rclcpp rclcpp_components std_msgs)
ament_target_dependencies(client_component rclcpp rclcpp_components example_interfaces)
ament_target_dependencies(server_component rclcpp rclcpp_components example_interfaces)

install(TARGETS
   talker_component
   comp_publisher
   listener_component
   comp_subscriber
   client_component
   comp_client
   server_component
   comp_server
  DESTINATION lib/${PROJECT_NAME}
  LIBRARY DESTINATION lib)
  
install(
  DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}
)



if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # uncomment the line when a copyright and license is not present in all source files
  #set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # uncomment the line when this package is not in a git repo
  #set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
