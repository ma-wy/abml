// Generated by gencpp from file gelsight_mini_ros/tracking_msg.msg
// DO NOT EDIT!


#ifndef GELSIGHT_MINI_ROS_MESSAGE_TRACKING_MSG_H
#define GELSIGHT_MINI_ROS_MESSAGE_TRACKING_MSG_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>

namespace gelsight_mini_ros
{
template <class ContainerAllocator>
struct tracking_msg_
{
  typedef tracking_msg_<ContainerAllocator> Type;

  tracking_msg_()
    : header()
    , marker_x()
    , marker_y()
    , marker_displacement_x()
    , marker_displacement_y()  {
    }
  tracking_msg_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , marker_x(_alloc)
    , marker_y(_alloc)
    , marker_displacement_x(_alloc)
    , marker_displacement_y(_alloc)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef std::vector<float, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<float>> _marker_x_type;
  _marker_x_type marker_x;

   typedef std::vector<float, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<float>> _marker_y_type;
  _marker_y_type marker_y;

   typedef std::vector<float, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<float>> _marker_displacement_x_type;
  _marker_displacement_x_type marker_displacement_x;

   typedef std::vector<float, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<float>> _marker_displacement_y_type;
  _marker_displacement_y_type marker_displacement_y;





  typedef boost::shared_ptr< ::gelsight_mini_ros::tracking_msg_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::gelsight_mini_ros::tracking_msg_<ContainerAllocator> const> ConstPtr;

}; // struct tracking_msg_

typedef ::gelsight_mini_ros::tracking_msg_<std::allocator<void> > tracking_msg;

typedef boost::shared_ptr< ::gelsight_mini_ros::tracking_msg > tracking_msgPtr;
typedef boost::shared_ptr< ::gelsight_mini_ros::tracking_msg const> tracking_msgConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::gelsight_mini_ros::tracking_msg_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::gelsight_mini_ros::tracking_msg_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::gelsight_mini_ros::tracking_msg_<ContainerAllocator1> & lhs, const ::gelsight_mini_ros::tracking_msg_<ContainerAllocator2> & rhs)
{
  return lhs.header == rhs.header &&
    lhs.marker_x == rhs.marker_x &&
    lhs.marker_y == rhs.marker_y &&
    lhs.marker_displacement_x == rhs.marker_displacement_x &&
    lhs.marker_displacement_y == rhs.marker_displacement_y;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::gelsight_mini_ros::tracking_msg_<ContainerAllocator1> & lhs, const ::gelsight_mini_ros::tracking_msg_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace gelsight_mini_ros

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::gelsight_mini_ros::tracking_msg_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::gelsight_mini_ros::tracking_msg_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::gelsight_mini_ros::tracking_msg_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::gelsight_mini_ros::tracking_msg_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::gelsight_mini_ros::tracking_msg_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::gelsight_mini_ros::tracking_msg_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::gelsight_mini_ros::tracking_msg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "8b99f4a1ff1377c066f07003f01617ae";
  }

  static const char* value(const ::gelsight_mini_ros::tracking_msg_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x8b99f4a1ff1377c0ULL;
  static const uint64_t static_value2 = 0x66f07003f01617aeULL;
};

template<class ContainerAllocator>
struct DataType< ::gelsight_mini_ros::tracking_msg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "gelsight_mini_ros/tracking_msg";
  }

  static const char* value(const ::gelsight_mini_ros::tracking_msg_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::gelsight_mini_ros::tracking_msg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# timestamp\n"
"Header header\n"
"\n"
"# position and displacement of markers\n"
"float32[] marker_x\n"
"float32[] marker_y\n"
"float32[] marker_displacement_x\n"
"float32[] marker_displacement_y\n"
"\n"
"================================================================================\n"
"MSG: std_msgs/Header\n"
"# Standard metadata for higher-level stamped data types.\n"
"# This is generally used to communicate timestamped data \n"
"# in a particular coordinate frame.\n"
"# \n"
"# sequence ID: consecutively increasing ID \n"
"uint32 seq\n"
"#Two-integer timestamp that is expressed as:\n"
"# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n"
"# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n"
"# time-handling sugar is provided by the client library\n"
"time stamp\n"
"#Frame this data is associated with\n"
"string frame_id\n"
;
  }

  static const char* value(const ::gelsight_mini_ros::tracking_msg_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::gelsight_mini_ros::tracking_msg_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.marker_x);
      stream.next(m.marker_y);
      stream.next(m.marker_displacement_x);
      stream.next(m.marker_displacement_y);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct tracking_msg_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::gelsight_mini_ros::tracking_msg_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::gelsight_mini_ros::tracking_msg_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "marker_x[]" << std::endl;
    for (size_t i = 0; i < v.marker_x.size(); ++i)
    {
      s << indent << "  marker_x[" << i << "]: ";
      Printer<float>::stream(s, indent + "  ", v.marker_x[i]);
    }
    s << indent << "marker_y[]" << std::endl;
    for (size_t i = 0; i < v.marker_y.size(); ++i)
    {
      s << indent << "  marker_y[" << i << "]: ";
      Printer<float>::stream(s, indent + "  ", v.marker_y[i]);
    }
    s << indent << "marker_displacement_x[]" << std::endl;
    for (size_t i = 0; i < v.marker_displacement_x.size(); ++i)
    {
      s << indent << "  marker_displacement_x[" << i << "]: ";
      Printer<float>::stream(s, indent + "  ", v.marker_displacement_x[i]);
    }
    s << indent << "marker_displacement_y[]" << std::endl;
    for (size_t i = 0; i < v.marker_displacement_y.size(); ++i)
    {
      s << indent << "  marker_displacement_y[" << i << "]: ";
      Printer<float>::stream(s, indent + "  ", v.marker_displacement_y[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // GELSIGHT_MINI_ROS_MESSAGE_TRACKING_MSG_H
