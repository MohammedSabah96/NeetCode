# Design an algorithm to encode a list of strings to a string.
# The encoded string is then sent over the network and
# is decoded back to the original list of strings.

# Example 1:
# Input: ["lint","code","love","you"]
# Output: ["lint","code","love","you"]
# Explanation:
# One possible encode method is: "lint:;code:;love:;you"

# Example 2:
# Input: ["we", "say", ":", "yes"]
# Output: ["we", "say", ":", "yes"]
# Explanation:
# One possible encode method is: "we:;say:;:::;yes"

class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    @staticmethod
    def encode(strs: list[str]) -> str:
        """
        @param: str: A string
        @return: dcodes a single string to a list of strings
        """
        encoded = ""
        for s in strs:
            encoded += s + ":;"

        return encoded[:-2]

    @staticmethod
    def decode(str_single: str) -> list[str]:
        return str_single.split(":;")


def encode(strs: list[str]) -> str:
    encoded = ""
    for s in strs:
        encoded += str(len(s)) + "#" + s

    return encoded


def decode(str_single: str) -> list[str]:
    decoded, i = [], 0

    while i < len(str_single):
        j = i
        while str_single[j] != "#":
            j += 1

        length = int(str_single[i:j])
        decoded.append(str_single[j + 1:j + 1 + length])
        i = j + 1 + length

    return decoded


def print_encode_decode_strings(encode_fun, decode_fun, strs):
    print(strs)
    encoded = encode_fun(list_of_strs)
    print(encoded)
    decoded = decode_fun(encoded)
    print(decoded)


sol = Solution()
list_of_strs = ["lint", "code", "love", "you"]
print_encode_decode_strings(sol.encode, sol.decode, list_of_strs)
print_encode_decode_strings(encode, decode, list_of_strs)
list_of_strs = ["we", "say", ":", "yes"]
print_encode_decode_strings(sol.encode, sol.decode, list_of_strs)
print_encode_decode_strings(encode, decode, list_of_strs)
