#include "trienode.h"
#include "trie.h"
#include <cassert>
#include <iostream>
#include <string>
#include <vector>

int main()
{
	std::vector<std::string> vecPositiveTestWords = { "abc", "cba", "bca", "bba", "abbccaa", "abcaabca", "aaabbbccc", "abcabc", "abc", "abba", "baba", "abbabaab" };
	std::vector<std::string> vecNegativeTestWords = { "ab", "cb", "bc", "bb", "abbcca", "abcaabcaa", "aaabbbcccc", "abcab", "abca", "aba", "bab", "abbaabbaab" };

	Trie trie;
	for (const std::string& word : vecPositiveTestWords)
	{
		trie.Put(word);
	}

	// Positive tests
	std::cout << "\nBeginning positive tests" << std::endl;
	for (const std::string& word : vecPositiveTestWords)
	{
		assert(trie.Contains(word));
	}
	std::cout << "\nPositive tests finished successfully.\n" << std::endl;

	// Negative tests
	std::cout << "\nBeginning negative tests" << std::endl;
	for (const std::string& word : vecNegativeTestWords)
	{
		assert(!trie.Contains(word));
	}
	std::cout << "\nNegative tests finished successfully.\n" << std::endl;
	return 0;
}


