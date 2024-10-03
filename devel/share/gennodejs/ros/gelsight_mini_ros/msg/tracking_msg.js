// Auto-generated. Do not edit!

// (in-package gelsight_mini_ros.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class tracking_msg {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.marker_x = null;
      this.marker_y = null;
      this.marker_displacement_x = null;
      this.marker_displacement_y = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('marker_x')) {
        this.marker_x = initObj.marker_x
      }
      else {
        this.marker_x = [];
      }
      if (initObj.hasOwnProperty('marker_y')) {
        this.marker_y = initObj.marker_y
      }
      else {
        this.marker_y = [];
      }
      if (initObj.hasOwnProperty('marker_displacement_x')) {
        this.marker_displacement_x = initObj.marker_displacement_x
      }
      else {
        this.marker_displacement_x = [];
      }
      if (initObj.hasOwnProperty('marker_displacement_y')) {
        this.marker_displacement_y = initObj.marker_displacement_y
      }
      else {
        this.marker_displacement_y = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type tracking_msg
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [marker_x]
    bufferOffset = _arraySerializer.float32(obj.marker_x, buffer, bufferOffset, null);
    // Serialize message field [marker_y]
    bufferOffset = _arraySerializer.float32(obj.marker_y, buffer, bufferOffset, null);
    // Serialize message field [marker_displacement_x]
    bufferOffset = _arraySerializer.float32(obj.marker_displacement_x, buffer, bufferOffset, null);
    // Serialize message field [marker_displacement_y]
    bufferOffset = _arraySerializer.float32(obj.marker_displacement_y, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type tracking_msg
    let len;
    let data = new tracking_msg(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [marker_x]
    data.marker_x = _arrayDeserializer.float32(buffer, bufferOffset, null)
    // Deserialize message field [marker_y]
    data.marker_y = _arrayDeserializer.float32(buffer, bufferOffset, null)
    // Deserialize message field [marker_displacement_x]
    data.marker_displacement_x = _arrayDeserializer.float32(buffer, bufferOffset, null)
    // Deserialize message field [marker_displacement_y]
    data.marker_displacement_y = _arrayDeserializer.float32(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    length += 4 * object.marker_x.length;
    length += 4 * object.marker_y.length;
    length += 4 * object.marker_displacement_x.length;
    length += 4 * object.marker_displacement_y.length;
    return length + 16;
  }

  static datatype() {
    // Returns string type for a message object
    return 'gelsight_mini_ros/tracking_msg';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '8b99f4a1ff1377c066f07003f01617ae';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # timestamp
    Header header
    
    # position and displacement of markers
    float32[] marker_x
    float32[] marker_y
    float32[] marker_displacement_x
    float32[] marker_displacement_y
    
    ================================================================================
    MSG: std_msgs/Header
    # Standard metadata for higher-level stamped data types.
    # This is generally used to communicate timestamped data 
    # in a particular coordinate frame.
    # 
    # sequence ID: consecutively increasing ID 
    uint32 seq
    #Two-integer timestamp that is expressed as:
    # * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
    # * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
    # time-handling sugar is provided by the client library
    time stamp
    #Frame this data is associated with
    string frame_id
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new tracking_msg(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.marker_x !== undefined) {
      resolved.marker_x = msg.marker_x;
    }
    else {
      resolved.marker_x = []
    }

    if (msg.marker_y !== undefined) {
      resolved.marker_y = msg.marker_y;
    }
    else {
      resolved.marker_y = []
    }

    if (msg.marker_displacement_x !== undefined) {
      resolved.marker_displacement_x = msg.marker_displacement_x;
    }
    else {
      resolved.marker_displacement_x = []
    }

    if (msg.marker_displacement_y !== undefined) {
      resolved.marker_displacement_y = msg.marker_displacement_y;
    }
    else {
      resolved.marker_displacement_y = []
    }

    return resolved;
    }
};

module.exports = tracking_msg;
