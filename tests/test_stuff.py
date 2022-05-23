from jebarasml.lib import try_me


def test_sum():
    test_list=[1,2,3]
    assert try_me(test_list) == 6
