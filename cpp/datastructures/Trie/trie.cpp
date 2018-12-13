#include "trienode.h"
#include "trie.h"
#include <cassert>
#include <iostream>
#include <string>
#include <vector>

int main()
{
	std::vector<std::string> vecPositiveTestWords = { "abc", "cba", "bca", "bba", "abbccaa", "abcaabca", "aaabbbccc", "abcabc", "abce", "abba", "baba", "abbabaab", "def" };
	std::vector<std::string> vecNegativeTestWords = { "ab", "cb", "bc", "bb", "abbcca", "abcaabcaa", "aaabbbcccc", "abcab", "abca", "aba", "bab", "abbaabbaab", "abdde" };

	Trie<int> trie;
	int i = 0;
	for (const std::string& word : vecPositiveTestWords)
	{
		trie.Put(word, i++);
	}

	// Positive tests
	i = 0;
	int value;
	std::cout << "\nBeginning positive tests" << std::endl;
	for (const std::string& word : vecPositiveTestWords)
	{
		assert(trie.Contains(word));
		assert(trie.GetValue(word, value));
		assert(value == i++);
	}
	std::cout << "Positive tests finished successfully.\n" << std::endl;

	// Negative tests
	std::cout << "\nBeginning negative tests" << std::endl;
	for (const std::string& word : vecNegativeTestWords)
	{
		assert(!trie.Contains(word));
		assert(!trie.GetValue(word, value));
	}
	std::cout << "Negative tests finished successfully.\n" << std::endl;

	// Erase tests
	i = 0;
	std::cout << "\nBeginning erase tests" << std::endl;
	for (const std::string& word : vecPositiveTestWords)
	{
		trie.Remove(word);
		assert(!trie.Contains(word));
		assert(!trie.GetValue(word, value));
		trie.Put(word, i);
		assert(trie.Contains(word));
		assert(trie.GetValue(word, value));
		assert(value == i++);
		trie.EraseRemove(word);
		assert(!trie.Contains(word));
		assert(!trie.GetValue(word, value));
	}
	std::cout << "Erasetests finished successfully.\n" << std::endl;



	return 0;
}
