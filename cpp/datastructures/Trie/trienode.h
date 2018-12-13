#ifndef  __TRIENODE_H__
#define __TRIENODE_H__

#include <map>
#include <memory>

template<typename T>
class TrieNode
{
	typedef std::shared_ptr<TrieNode> TrieNodePtr;
	typedef std::map<char, TrieNodePtr> ChildrenMap;
	typedef std::shared_ptr<ChildrenMap> ChildrenMapPtr;

public:
	TrieNode() :
		m_bHasValue(false),
		m_children(std::make_shared<ChildrenMap>())
	{
	}

	T GetValue()
	{
		return m_value;
	}

	void SetValue(T value)
	{
		m_value = value;
		m_bHasValue = true;
	}

	ChildrenMapPtr GetChildren()
	{
		return m_children;
	}

	bool HasValue()
	{
		return m_bHasValue;
	}

	void HasValue(bool bHasValue)
	{
		m_bHasValue = bHasValue;
	}

private:
	bool m_bHasValue;
	ChildrenMapPtr m_children;
	T m_value;
};

#endif // ! __TRIENODE_H__

