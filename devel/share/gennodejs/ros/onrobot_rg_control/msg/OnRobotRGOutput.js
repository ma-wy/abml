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

class OnRobotRGOutput {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.rGFR = null;
      this.rGWD = null;
      this.rCTR = null;
    }
    else {
      if (initObj.hasOwnProperty('rGFR')) {
        this.rGFR = initObj.rGFR
      }
      else {
        this.rGFR = 0;
      }
      if (initObj.hasOwnProperty('rGWD')) {
        this.rGWD = initObj.rGWD
      }
      else {
        this.rGWD = 0;
      }
      if (initObj.hasOwnProperty('rCTR')) {
        this.rCTR = initObj.rCTR
      }
      else {
        this.rCTR = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type OnRobotRGOutput
    // Serialize message field [rGFR]
    bufferOffset = _serializer.uint16(obj.rGFR, buffer, bufferOffset);
    // Serialize message field [rGWD]
    bufferOffset = _serializer.uint16(obj.rGWD, buffer, bufferOffset);
    // Serialize message field [rCTR]
    bufferOffset = _serializer.uint8(obj.rCTR, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type OnRobotRGOutput
    let len;
    let data = new OnRobotRGOutput(null);
    // Deserialize message field [rGFR]
    data.rGFR = _deserializer.uint16(buffer, bufferOffset);
    // Deserialize message field [rGWD]
    data.rGWD = _deserializer.uint16(buffer, bufferOffset);
    // Deserialize message field [rCTR]
    data.rCTR = _deserializer.uint8(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 5;
  }

  static datatype() {
    // Returns string type for a message object
    return 'onrobot_rg_control/OnRobotRGOutput';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'd99680fed3cb1854614e74f47d8e8f52';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # rGFR : The target force to be reached when gripping and holding a workpiece.
    #        It must be provided in 1/10th Newtons.
    #        The valid range is 0 to 400 for the RG2 and 0 to 1200 for the RG6.
    
    uint16 rGFR
    
    # rGWD : The target width between the finger to be moved to and maintained.
    #        It must be provided in 1/10th millimeters.
    #        The valid range is 0 to 1100 for the RG2 and 0 to 1600 for the RG6.
    #        Please note that the target width should be provided corrected for any fingertip offset,
    #        as it is measured between the insides of the aluminum fingers.
    
    uint16 rGWD
    
    # rCTR : The control field is used to start and stop gripper motion.
    #        Only one option should be set at a time.
    #        Please note that the gripper will not start a new motion
    #        before the one currently being executed is done (see busy flag in the Status field).
    # 0x0001 - grip
    #          Start the motion, with the preset target force and width.
    #          Width is calculated without the fingertip offset.
    #          Please note that the gripper will ignore this command
    #          if the busy flag is set in the status field.
    # 0x0008 - stop
    #          Stop the current motion.
    # 0x0010 - grip_w_offset
    #          Same as grip, but width is calculated with the set fingertip offset.
    
    uint8 rCTR
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new OnRobotRGOutput(null);
    if (msg.rGFR !== undefined) {
      resolved.rGFR = msg.rGFR;
    }
    else {
      resolved.rGFR = 0
    }

    if (msg.rGWD !== undefined) {
      resolved.rGWD = msg.rGWD;
    }
    else {
      resolved.rGWD = 0
    }

    if (msg.rCTR !== undefined) {
      resolved.rCTR = msg.rCTR;
    }
    else {
      resolved.rCTR = 0
    }

    return resolved;
    }
};

module.exports = OnRobotRGOutput;
