const hre = require("hardhat");

async function main() {
  const BatchHashStore = await hre.ethers.getContractFactory("BatchHashStore");
  const contract = await BatchHashStore.deploy();
  await contract.deployed();
  console.log("BatchHashStore deployed to:", contract.address);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
