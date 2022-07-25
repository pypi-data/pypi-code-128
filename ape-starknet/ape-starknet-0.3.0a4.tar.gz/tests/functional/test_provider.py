import time

import pytest
from starkware.starknet.public.abi import get_selector_from_name

from ape_starknet.utils import is_checksum_address


def test_get_nonce(provider, account, contract):
    initial_nonce = provider.get_nonce(account.address)

    # Transact to increase nonce
    contract.increase_balance(account.address, 123, sender=account)

    actual = provider.get_nonce(account.address)
    assert actual == initial_nonce + 1


def test_get_block(provider, contract):
    _ = contract  # Contract fixture used to increase blocks (since deploys happen)
    latest_block_0 = provider.get_block("latest")
    latest_block_1 = provider.get_block(-1)
    latest_block_2 = provider.get_block(latest_block_0.number)
    assert latest_block_0.hash == latest_block_1.hash == latest_block_2.hash


def test_get_negative_block_number(account, provider, contract):
    start_block = provider.get_block("latest").number
    for _ in range(3):
        # Mine 3 blocks
        contract.increase_balance(account.address, 12, sender=account)

    block = provider.get_block(-2)
    assert block.number == start_block + 2


def test_get_block_negative_number_resulting_less_than_zero(provider, contract):
    _ = contract  # Contract fixture used to increase blocks (since deploys happen)
    latest_block_number = provider.get_block("latest").number
    value = -1000000000000000
    with pytest.raises(ValueError) as err:
        provider.get_block(value)

    expected_block_number = latest_block_number + value + 1
    assert (
        str(err.value)
        == f"Negative block number '{expected_block_number}' results in non-existent block."
    )


def test_get_transactions_by_block(provider, account, contract):
    # Transact to create data.
    expected_value = 123
    contract.increase_balance(account.address, expected_value, sender=account)

    transactions = [t for t in provider.get_transactions_by_block("latest")]

    expected_chain_id = provider.chain_id
    expected_abi = [
        a for a in account.get_contract_type().mutable_methods if a.name == "__execute__"
    ][0]
    expected_nonce = account.nonce - 1
    assert len(transactions) == 1
    assert transactions[0].chain_id == expected_chain_id
    assert transactions[0].method_abi == expected_abi
    assert transactions[0].receiver == account.address
    assert transactions[0].value == 0
    assert is_checksum_address(transactions[0].receiver)
    expected_data = [
        1,
        provider.starknet.encode_address(contract.address),
        get_selector_from_name("increase_balance"),
        0,
        2,
        2,
        provider.starknet.encode_address(account.address),
        expected_value,
        expected_nonce,
    ]
    assert transactions[0].data == expected_data


def test_set_timestamp(provider, account, contract):
    start_time = provider.get_block("pending").timestamp
    provider.set_timestamp(start_time + 8600)
    contract.increase_balance(account.address, 123, sender=account)
    curr_time = time.time()
    assert pytest.approx(curr_time + 8600) == provider.get_block("latest").timestamp
