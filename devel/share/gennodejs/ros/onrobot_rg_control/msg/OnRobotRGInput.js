// Auto-generated. Do not edit!

// (in-package onrobot_rg_control.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class OnRobotRGInput {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.gFOF = null;
      this.gGWD = null;
      this.gSTA = null;
      this.gWDF = null;
    }
    else {
      if (initObj.hasOwnProperty('gFOF')) {
        this.gFOF = initObj.gFOF
      }
      else {
        this.gFOF = 0;
      }
      if (initObj.hasOwnProperty('gGWD')) {
        this.gGWD = initObj.gGWD
      }
      else {
        this.gGWD = 0;
      }
      if (initObj.hasOwnProperty('gSTA')) {
        this.gSTA = initObj.gSTA
      }
      else {
        this.gSTA = 0;
      }
      if (initObj.hasOwnProperty('gWDF')) {
        this.gWDF = initObj.gWDF
      }
      else {
        this.gWDF = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type OnRobotRGInput
    // Serialize message field [gFOF]
    bufferOffset = _serializer.uint16(obj.gFOF, buffer, bufferOffset);
    // Serialize message field [gGWD]
    bufferOffset = _serializer.uint16(obj.gGWD, buffer, bufferOffset);
    // Serialize message field [gSTA]
    bufferOffset = _serializer.uint8(obj.gSTA, buffer, bufferOffset);
    // Serialize message field [gWDF]
    bufferOffset = _serializer.uint16(obj.gWDF, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type OnRobotRGInput
    let len;
    let data = new OnRobotRGInput(null);
    // Deserialize message field [gFOF]
    data.gFOF = _deserializer.uint16(buffer, bufferOffset);
    // Deserialize message field [gGWD]
    data.gGWD = _deserializer.uint16(buffer, bufferOffset);
    // Deserialize message field [gSTA]
    data.gSTA = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [gWDF]
    data.gWDF = _deserializer.uint16(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 7;
  }

  static datatype() {
    // Returns string type for a message object
    return 'onrobot_rg_control/OnRobotRGInput';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '94435113a24b6809371af29f68843bdb';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # gFOF : Current fingertip offset in 1/10 millimeters. The value is a signed two's complement number.
    
    uint16 gFOF
    
    # gGWD : Current width between the gripper fingers in 1/10 millimeters.
    #        The width is provided without any fingertip offset, as it is measured between the insides of the aluminum fingers.
    
    uint16 gGWD
    
    # gSTA : Current device status, which indicates the status of the gripper and its motion.
    # Bit       - Name              - Description
    # 0 (LSB)   - Busy              - High (1) when a motion is ongoing, low (0) when not. The gripper will only accept new commands when this flag is low.
    # 1         - Grip detected     - High (1) when an internal- or external grip is detected.
    # 2         - S1 pushed         - High (1) when safety switch 1 is pushed.
    # 3         - S1 trigged        - High (1) when safety circuit 1 is activated. The gripper will not move while this flag is high.
    # 4         - S2 pushed         - High (1) when safety switch 2 is pushed.
    # 5         - S2 trigged        - High (1) when safety circuit 2 is activated. The gripper will not move while this flag is high.
    # 6         - Safety error      - High (1) when on power on any of the safety switch is pushed.
    # 7 - 15    - Reserved          - Not used.
    
    uint8 gSTA
    
    # gWDF : Current width between the gripper fingers in 1/10 millimeters.
    #        The set fingertip offset is considered.
    
    uint16 gWDF
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new OnRobotRGInput(null);
    if (msg.gFOF !== undefined) {
      resolved.gFOF = msg.gFOF;
    }
    else {
      resolved.gFOF = 0
    }

    if (msg.gGWD !== undefined) {
      resolved.gGWD = msg.gGWD;
    }
    else {
      resolved.gGWD = 0
    }

    if (msg.gSTA !== undefined) {
      resolved.gSTA = msg.gSTA;
    }
    else {
      resolved.gSTA = 0
    }

    if (msg.gWDF !== undefined) {
      resolved.gWDF = msg.gWDF;
    }
    else {
      resolved.gWDF = 0
    }

    return resolved;
    }
};

module.exports = OnRobotRGInput;
