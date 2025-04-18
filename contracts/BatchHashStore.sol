// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract BatchHashStore {
    event BatchStored(address indexed sender, bytes32 hash, uint256 timestamp);

    function storeBatchHash(bytes32 batchHash) external {
        emit BatchStored(msg.sender, batchHash, block.timestamp);
    }
}
