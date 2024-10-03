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

class judging_msg {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.is_contact = null;
      this.is_overforced = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('is_contact')) {
        this.is_contact = initObj.is_contact
      }
      else {
        this.is_contact = false;
      }
      if (initObj.hasOwnProperty('is_overforced')) {
        this.is_overforced = initObj.is_overforced
      }
      else {
        this.is_overforced = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type judging_msg
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [is_contact]
    bufferOffset = _serializer.bool(obj.is_contact, buffer, bufferOffset);
    // Serialize message field [is_overforced]
    bufferOffset = _serializer.bool(obj.is_overforced, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type judging_msg
    let len;
    let data = new judging_msg(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [is_contact]
    data.is_contact = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [is_overforced]
    data.is_overforced = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    return length + 2;
  }

  static datatype() {
    // Returns string type for a message object
    return 'gelsight_mini_ros/judging_msg';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '10ed4c6e740e87d5c0e7f8d06f6ac17c';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # timestamp
    Header header
    
    # contact and over-forced judgement
    bool is_contact
    bool is_overforced
    
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
    const resolved = new judging_msg(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.is_contact !== undefined) {
      resolved.is_contact = msg.is_contact;
    }
    else {
      resolved.is_contact = false
    }

    if (msg.is_overforced !== undefined) {
      resolved.is_overforced = msg.is_overforced;
    }
    else {
      resolved.is_overforced = false
    }

    return resolved;
    }
};

module.exports = judging_msg;
