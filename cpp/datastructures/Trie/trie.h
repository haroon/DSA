#ifndef  __TRIE_H__
#define __TRIE_H__

#include "trienode.h"
#include <memory>
#include <string>

class Trie
{
public:
	Trie() :
		m_pRoot(std::make_shared<TrieNode>())
	{

	}

	bool Contains(const std::string& key)
	{
		ChildrenMapPtr children = m_pRoot->GetChildren();
		for (size_t idx = 0; idx < key.size(); ++idx)
		{
			char keyChar = key[idx];
			auto it = children->find(keyChar);
			if (it == children->end())
			{
				return false;
			}
			if (idx == key.size() - 1)
			{
				return it->second->IsWord();
			}
			children = it->second->GetChildren();
		}
		return true;
	}

	void Put(const std::string& key)
	{
		ChildrenMapPtr children = m_pRoot->GetChildren();
		for (size_t idx = 0; idx < key.size(); ++idx)
		{
			char keyChar = key[idx];
			auto it = children->find(keyChar);
			TrieNodePtr pNode;
			if (it == children->end())
			{
				pNode = std::make_shared<TrieNode>();
				children->emplace(keyChar, pNode);
			}
			else
			{
				pNode = it->second;
			}
			if (idx == key.size() - 1)
			{
				pNode->SetWord(true);
			}
			else
			{
				children = pNode->GetChildren();
			}
		}
	}

private:
	TrieNodePtr m_pRoot;
};

#endif // ! __TRIE_H__

