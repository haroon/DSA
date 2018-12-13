#ifndef  __TRIE_H__
#define __TRIE_H__

#include "trienode.h"
#include <memory>
#include <stack>
#include <string>

template<typename T>
class Trie
{
	typedef std::shared_ptr< TrieNode<T> > TrieNodePtr;
	typedef std::map<char, TrieNodePtr> ChildrenMap;
	typedef std::shared_ptr<ChildrenMap> ChildrenMapPtr;

public:
	Trie() :
		m_pRoot(std::make_shared< TrieNode<T> >())
	{
	}

	bool Contains(const std::string& key)
	{
		TrieNodePtr pNode = Find(key);
		return pNode && pNode->HasValue();
	}

	bool GetValue(const std::string& key, T& value)
	{
		TrieNodePtr pNode = Find(key);
		if (pNode && pNode->HasValue())
		{
			value = pNode->GetValue();
			return true;
		}
		return false;
	}

	void Put(const std::string& key, T value)
	{
		ChildrenMapPtr children = m_pRoot->GetChildren();
		for (size_t idx = 0; idx < key.size(); ++idx)
		{
			char keyChar = key[idx];
			auto it = children->find(keyChar);
			TrieNodePtr pNode;
			if (it == children->end())
			{
				pNode = std::make_shared< TrieNode<T> >();
				children->emplace(keyChar, pNode);
			}
			else
			{
				pNode = it->second;
			}
			if (idx == key.size() - 1)
			{
				pNode->SetValue(value);
			}
			else
			{
				children = pNode->GetChildren();
			}
		}
	}

	void Remove(const std::string& key)
	{
		TrieNodePtr pNode = Find(key);
		if (pNode)
		{
			pNode->HasValue(false);
		}
	}

	void EraseRemove(const std::string& key)
	{
		std::stack< std::pair<char, TrieNodePtr> > path;
		path.push(std::make_pair(' ', m_pRoot));
		ChildrenMapPtr children = m_pRoot->GetChildren();
		for (size_t idx = 0; idx < key.size(); ++idx)
		{
			char keyChar = key[idx];
			auto it = children->find(keyChar);
			// Key mismatch, this key doesn't exist. Return!
			if (it == children->end())
			{
				return;
			}
			children = it->second->GetChildren();
			path.push(std::make_pair(it->first, it->second));
		}

		path.top().second->HasValue(false);
		while
		(
			path.size() > 1 &&
			!path.top().second->HasValue() &&
			path.top().second->GetChildren()->size() == 0
		)
		{
			char keyChar = path.top().first;
			path.pop();
			path.top().second->GetChildren()->erase(keyChar);
		}
	}

private:
	TrieNodePtr Find(const std::string& key)
	{
		ChildrenMapPtr children = m_pRoot->GetChildren();
		typename ChildrenMap::iterator it;
		for (size_t idx = 0; idx < key.size(); ++idx)
		{
			char keyChar = key[idx];
			it = children->find(keyChar);
			if (it == children->end())
			{
				return nullptr;
			}
			children = it->second->GetChildren();
		}
		return it->second;
	}

	TrieNodePtr m_pRoot;
};

#endif // ! __TRIE_H__

