// Auto-generated. Do not edit!

// (in-package handover.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let geometry_msgs = _finder('geometry_msgs');
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class hand_mp {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.handedness = null;
      this.wrist = null;
      this.thumb_tip = null;
      this.index_tip = null;
      this.middle_tip = null;
      this.ring_tip = null;
      this.pinky_tip = null;
      this.index_mcp = null;
      this.middle_mcp = null;
      this.ring_mcp = null;
      this.pinky_mcp = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('handedness')) {
        this.handedness = initObj.handedness
      }
      else {
        this.handedness = new std_msgs.msg.String();
      }
      if (initObj.hasOwnProperty('wrist')) {
        this.wrist = initObj.wrist
      }
      else {
        this.wrist = new geometry_msgs.msg.Point();
      }
      if (initObj.hasOwnProperty('thumb_tip')) {
        this.thumb_tip = initObj.thumb_tip
      }
      else {
        this.thumb_tip = new geometry_msgs.msg.Point();
      }
      if (initObj.hasOwnProperty('index_tip')) {
        this.index_tip = initObj.index_tip
      }
      else {
        this.index_tip = new geometry_msgs.msg.Point();
      }
      if (initObj.hasOwnProperty('middle_tip')) {
        this.middle_tip = initObj.middle_tip
      }
      else {
        this.middle_tip = new geometry_msgs.msg.Point();
      }
      if (initObj.hasOwnProperty('ring_tip')) {
        this.ring_tip = initObj.ring_tip
      }
      else {
        this.ring_tip = new geometry_msgs.msg.Point();
      }
      if (initObj.hasOwnProperty('pinky_tip')) {
        this.pinky_tip = initObj.pinky_tip
      }
      else {
        this.pinky_tip = new geometry_msgs.msg.Point();
      }
      if (initObj.hasOwnProperty('index_mcp')) {
        this.index_mcp = initObj.index_mcp
      }
      else {
        this.index_mcp = new geometry_msgs.msg.Point();
      }
      if (initObj.hasOwnProperty('middle_mcp')) {
        this.middle_mcp = initObj.middle_mcp
      }
      else {
        this.middle_mcp = new geometry_msgs.msg.Point();
      }
      if (initObj.hasOwnProperty('ring_mcp')) {
        this.ring_mcp = initObj.ring_mcp
      }
      else {
        this.ring_mcp = new geometry_msgs.msg.Point();
      }
      if (initObj.hasOwnProperty('pinky_mcp')) {
        this.pinky_mcp = initObj.pinky_mcp
      }
      else {
        this.pinky_mcp = new geometry_msgs.msg.Point();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type hand_mp
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [handedness]
    bufferOffset = std_msgs.msg.String.serialize(obj.handedness, buffer, bufferOffset);
    // Serialize message field [wrist]
    bufferOffset = geometry_msgs.msg.Point.serialize(obj.wrist, buffer, bufferOffset);
    // Serialize message field [thumb_tip]
    bufferOffset = geometry_msgs.msg.Point.serialize(obj.thumb_tip, buffer, bufferOffset);
    // Serialize message field [index_tip]
    bufferOffset = geometry_msgs.msg.Point.serialize(obj.index_tip, buffer, bufferOffset);
    // Serialize message field [middle_tip]
    bufferOffset = geometry_msgs.msg.Point.serialize(obj.middle_tip, buffer, bufferOffset);
    // Serialize message field [ring_tip]
    bufferOffset = geometry_msgs.msg.Point.serialize(obj.ring_tip, buffer, bufferOffset);
    // Serialize message field [pinky_tip]
    bufferOffset = geometry_msgs.msg.Point.serialize(obj.pinky_tip, buffer, bufferOffset);
    // Serialize message field [index_mcp]
    bufferOffset = geometry_msgs.msg.Point.serialize(obj.index_mcp, buffer, bufferOffset);
    // Serialize message field [middle_mcp]
    bufferOffset = geometry_msgs.msg.Point.serialize(obj.middle_mcp, buffer, bufferOffset);
    // Serialize message field [ring_mcp]
    bufferOffset = geometry_msgs.msg.Point.serialize(obj.ring_mcp, buffer, bufferOffset);
    // Serialize message field [pinky_mcp]
    bufferOffset = geometry_msgs.msg.Point.serialize(obj.pinky_mcp, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type hand_mp
    let len;
    let data = new hand_mp(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [handedness]
    data.handedness = std_msgs.msg.String.deserialize(buffer, bufferOffset);
    // Deserialize message field [wrist]
    data.wrist = geometry_msgs.msg.Point.deserialize(buffer, bufferOffset);
    // Deserialize message field [thumb_tip]
    data.thumb_tip = geometry_msgs.msg.Point.deserialize(buffer, bufferOffset);
    // Deserialize message field [index_tip]
    data.index_tip = geometry_msgs.msg.Point.deserialize(buffer, bufferOffset);
    // Deserialize message field [middle_tip]
    data.middle_tip = geometry_msgs.msg.Point.deserialize(buffer, bufferOffset);
    // Deserialize message field [ring_tip]
    data.ring_tip = geometry_msgs.msg.Point.deserialize(buffer, bufferOffset);
    // Deserialize message field [pinky_tip]
    data.pinky_tip = geometry_msgs.msg.Point.deserialize(buffer, bufferOffset);
    // Deserialize message field [index_mcp]
    data.index_mcp = geometry_msgs.msg.Point.deserialize(buffer, bufferOffset);
    // Deserialize message field [middle_mcp]
    data.middle_mcp = geometry_msgs.msg.Point.deserialize(buffer, bufferOffset);
    // Deserialize message field [ring_mcp]
    data.ring_mcp = geometry_msgs.msg.Point.deserialize(buffer, bufferOffset);
    // Deserialize message field [pinky_mcp]
    data.pinky_mcp = geometry_msgs.msg.Point.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    length += std_msgs.msg.String.getMessageSize(object.handedness);
    return length + 240;
  }

  static datatype() {
    // Returns string type for a message object
    return 'handover/hand_mp';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'c180baaf221b3c9ea1b674a724ca2e79';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    Header header
    std_msgs/String handedness
    geometry_msgs/Point wrist
    geometry_msgs/Point thumb_tip
    geometry_msgs/Point index_tip
    geometry_msgs/Point middle_tip
    geometry_msgs/Point ring_tip
    geometry_msgs/Point pinky_tip
    geometry_msgs/Point index_mcp
    geometry_msgs/Point middle_mcp
    geometry_msgs/Point ring_mcp
    geometry_msgs/Point pinky_mcp
    
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
    
    ================================================================================
    MSG: std_msgs/String
    string data
    
    ================================================================================
    MSG: geometry_msgs/Point
    # This contains the position of a point in free space
    float64 x
    float64 y
    float64 z
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new hand_mp(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.handedness !== undefined) {
      resolved.handedness = std_msgs.msg.String.Resolve(msg.handedness)
    }
    else {
      resolved.handedness = new std_msgs.msg.String()
    }

    if (msg.wrist !== undefined) {
      resolved.wrist = geometry_msgs.msg.Point.Resolve(msg.wrist)
    }
    else {
      resolved.wrist = new geometry_msgs.msg.Point()
    }

    if (msg.thumb_tip !== undefined) {
      resolved.thumb_tip = geometry_msgs.msg.Point.Resolve(msg.thumb_tip)
    }
    else {
      resolved.thumb_tip = new geometry_msgs.msg.Point()
    }

    if (msg.index_tip !== undefined) {
      resolved.index_tip = geometry_msgs.msg.Point.Resolve(msg.index_tip)
    }
    else {
      resolved.index_tip = new geometry_msgs.msg.Point()
    }

    if (msg.middle_tip !== undefined) {
      resolved.middle_tip = geometry_msgs.msg.Point.Resolve(msg.middle_tip)
    }
    else {
      resolved.middle_tip = new geometry_msgs.msg.Point()
    }

    if (msg.ring_tip !== undefined) {
      resolved.ring_tip = geometry_msgs.msg.Point.Resolve(msg.ring_tip)
    }
    else {
      resolved.ring_tip = new geometry_msgs.msg.Point()
    }

    if (msg.pinky_tip !== undefined) {
      resolved.pinky_tip = geometry_msgs.msg.Point.Resolve(msg.pinky_tip)
    }
    else {
      resolved.pinky_tip = new geometry_msgs.msg.Point()
    }

    if (msg.index_mcp !== undefined) {
      resolved.index_mcp = geometry_msgs.msg.Point.Resolve(msg.index_mcp)
    }
    else {
      resolved.index_mcp = new geometry_msgs.msg.Point()
    }

    if (msg.middle_mcp !== undefined) {
      resolved.middle_mcp = geometry_msgs.msg.Point.Resolve(msg.middle_mcp)
    }
    else {
      resolved.middle_mcp = new geometry_msgs.msg.Point()
    }

    if (msg.ring_mcp !== undefined) {
      resolved.ring_mcp = geometry_msgs.msg.Point.Resolve(msg.ring_mcp)
    }
    else {
      resolved.ring_mcp = new geometry_msgs.msg.Point()
    }

    if (msg.pinky_mcp !== undefined) {
      resolved.pinky_mcp = geometry_msgs.msg.Point.Resolve(msg.pinky_mcp)
    }
    else {
      resolved.pinky_mcp = new geometry_msgs.msg.Point()
    }

    return resolved;
    }
};

module.exports = hand_mp;
