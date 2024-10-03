// Auto-generated. Do not edit!

// (in-package llm_grasping.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class RadianToAngleRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.radian = null;
    }
    else {
      if (initObj.hasOwnProperty('radian')) {
        this.radian = initObj.radian
      }
      else {
        this.radian = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type RadianToAngleRequest
    // Serialize message field [radian]
    bufferOffset = _serializer.float64(obj.radian, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type RadianToAngleRequest
    let len;
    let data = new RadianToAngleRequest(null);
    // Deserialize message field [radian]
    data.radian = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 8;
  }

  static datatype() {
    // Returns string type for a service object
    return 'llm_grasping/RadianToAngleRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '0e9eb57682bb3c42defb75c34d25e755';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float64 radian
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new RadianToAngleRequest(null);
    if (msg.radian !== undefined) {
      resolved.radian = msg.radian;
    }
    else {
      resolved.radian = 0.0
    }

    return resolved;
    }
};

class RadianToAngleResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.angle = null;
      this.success = null;
    }
    else {
      if (initObj.hasOwnProperty('angle')) {
        this.angle = initObj.angle
      }
      else {
        this.angle = 0.0;
      }
      if (initObj.hasOwnProperty('success')) {
        this.success = initObj.success
      }
      else {
        this.success = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type RadianToAngleResponse
    // Serialize message field [angle]
    bufferOffset = _serializer.float64(obj.angle, buffer, bufferOffset);
    // Serialize message field [success]
    bufferOffset = _serializer.bool(obj.success, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type RadianToAngleResponse
    let len;
    let data = new RadianToAngleResponse(null);
    // Deserialize message field [angle]
    data.angle = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [success]
    data.success = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 9;
  }

  static datatype() {
    // Returns string type for a service object
    return 'llm_grasping/RadianToAngleResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'e8773bcd58191e43d4baf3dbd02e77e4';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float64 angle
    bool success
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new RadianToAngleResponse(null);
    if (msg.angle !== undefined) {
      resolved.angle = msg.angle;
    }
    else {
      resolved.angle = 0.0
    }

    if (msg.success !== undefined) {
      resolved.success = msg.success;
    }
    else {
      resolved.success = false
    }

    return resolved;
    }
};

module.exports = {
  Request: RadianToAngleRequest,
  Response: RadianToAngleResponse,
  md5sum() { return '8dd47fc5494973709ed579a85c77ce44'; },
  datatype() { return 'llm_grasping/RadianToAngle'; }
};
