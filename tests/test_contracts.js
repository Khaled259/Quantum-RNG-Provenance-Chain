const { expect } = require('chai');
const { ethers } = require('hardhat');

describe('BatchHashStore', function () {
  it('emits event on store', async function () {
    const [owner] = await ethers.getSigners();
    const Store = await ethers.getContractFactory('BatchHashStore');
    const store = await Store.deploy();
    await expect(store.storeBatchHash(ethers.utils.formatBytes32String('abc')))
      .to.emit(store, 'BatchStored')
      .withArgs(owner.address, ethers.utils.formatBytes32String('abc'), anyValue);
  });
});
