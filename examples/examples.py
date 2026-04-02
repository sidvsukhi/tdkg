from tdkg import TimeDecayGraph
import time

def simulate_user_memory():
    g = TimeDecayGraph(decay_lambda=0.1)

    # Simulating user interactions over time
    g.add("User is preparing for Amazon SDE interview")
    time.sleep(1)

    g.add("User is interested in system design")
    time.sleep(1)

    g.add("User is learning LLD and OOP design")
    time.sleep(1)

    g.add("User likes Python for backend development")

    print("\n🔍 Query: 'system design'")
    results = g.query("system design")
    print(results)

    print("\n📊 Top memory nodes:")
    print(g.get_top_k())

if __name__ == "__main__":
    simulate_user_memory()