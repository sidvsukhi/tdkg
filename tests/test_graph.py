# tests/test_graph.py

from tdkg import TimeDecayGraph
import time


def test_add_and_query():
    g = TimeDecayGraph()
    g.add("AI systems design")

    results = g.query("systems")
    assert len(results) > 0


def test_real_world_chat_memory():
    """
    Simulates an AI assistant memory where irrelevant info should fade
    and important/recent info should dominate.
    """
    g = TimeDecayGraph(decay_lambda=1.0)

    # Step 1: Add mixed context (like a real chat)
    g.add("User likes pizza")
    g.add("User is preparing for Amazon system design interview")
    g.add("User watched a movie yesterday")

    # Step 2: Simulate time passing (decay old/unused info)
    time.sleep(1)
    g.decay()

    # Step 3: Reinforce important topic (user keeps asking about interview)
    g.query("system design")
    g.query("interview")

    # Step 4: Get top memory
    top_nodes = g.get_top_k(2)
    top_contents = [n.content for n in top_nodes]

    # Expect interview-related memory to dominate
    assert any("interview" in content.lower() for content in top_contents)

    # Step 5: Prune weak/irrelevant memory
    g.prune(threshold=0.5)

    remaining_contents = [n.content for n in g.get_top_k(10)]

    # Ensure less relevant info (like movie) is likely removed
    assert not any("movie" in content.lower() for content in remaining_contents)