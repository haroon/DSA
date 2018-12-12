#ifndef  __TRIENODE_H__
#define __TRIENODE_H__

#include <map>
#include <memory>

class TrieNode;
typedef std::shared_ptr<TrieNode> TrieNodePtr;
typedef std::map<char, TrieNodePtr> ChildrenMap;
typedef std::shared_ptr<ChildrenMap> ChildrenMapPtr;


class TrieNode
{
public:
	TrieNode() :
		m_bIsWord(false),
		m_children(std::make_shared<ChildrenMap>())
	{
	}

	ChildrenMapPtr GetChildren()
	{
		return m_children;
	}

	bool IsWord()
	{
		return m_bIsWord;
	}

	void SetWord(bool bIsWord)
	{
		m_bIsWord = bIsWord;
	}

private:
	bool m_bIsWord;
	ChildrenMapPtr m_children;
};

#endif // ! __TRIENODE_H__

