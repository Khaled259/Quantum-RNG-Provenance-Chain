#!/usr/bin/env node
const { ethers } = require("ethers");
const yargs = require("yargs");
require("dotenv").config();

async function main() {
  const argv = yargs.option('hash', {type: 'string', describe: 'Batch hash hex'}).help().argv;
  if (!argv.hash) { console.error("--hash required"); process.exit(1);}  

  const provider = new ethers.providers.JsonRpcProvider(process.env.RPC_URL);
  const wallet = new ethers.Wallet(process.env.PRIVATE_KEY, provider);
  const abi = ["function storeBatchHash(bytes32)", "event BatchStored(address,bytes32,uint256)"];
  const address = process.env.CONTRACT_ADDRESS;
  const contract = new ethers.Contract(address, abi, wallet);

  const tx = await contract.storeBatchHash(argv.hash);
  console.log("Transaction sent:", tx.hash);
  await tx.wait();
  console.log("Stored hash on-chain");
}

main();
