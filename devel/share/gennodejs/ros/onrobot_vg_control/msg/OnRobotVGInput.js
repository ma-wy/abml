// Auto-generated. Do not edit!

// (in-package onrobot_vg_control.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class OnRobotVGInput {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.gVCA = null;
      this.gVCB = null;
    }
    else {
      if (initObj.hasOwnProperty('gVCA')) {
        this.gVCA = initObj.gVCA
      }
      else {
        this.gVCA = 0;
      }
      if (initObj.hasOwnProperty('gVCB')) {
        this.gVCB = initObj.gVCB
      }
      else {
        this.gVCB = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type OnRobotVGInput
    // Serialize message field [gVCA]
    bufferOffset = _serializer.uint16(obj.gVCA, buffer, bufferOffset);
    // Serialize message field [gVCB]
    bufferOffset = _serializer.uint16(obj.gVCB, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type OnRobotVGInput
    let len;
    let data = new OnRobotVGInput(null);
    // Deserialize message field [gVCA]
    data.gVCA = _deserializer.uint16(buffer, bufferOffset);
    // Deserialize message field [gVCB]
    data.gVCB = _deserializer.uint16(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 4;
  }

  static datatype() {
    // Returns string type for a message object
    return 'onrobot_vg_control/OnRobotVGInput';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '3b28006a7c1a9b8e6a658a70e5ab4a0d';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # gVCA : Current vacuum value on Channel A.
    #        The vacuum is provided in 1/1000 of relative vacuum.
    #        Please note that this differs from the setpoint given in percent,
    #        as extra accuracy is desirable on the actual vacuum.
    
    uint16 gVCA
    
    # gVCB : Same as the one of channel A.
    
    uint16 gVCB
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new OnRobotVGInput(null);
    if (msg.gVCA !== undefined) {
      resolved.gVCA = msg.gVCA;
    }
    else {
      resolved.gVCA = 0
    }

    if (msg.gVCB !== undefined) {
      resolved.gVCB = msg.gVCB;
    }
    else {
      resolved.gVCB = 0
    }

    return resolved;
    }
};

module.exports = OnRobotVGInput;
