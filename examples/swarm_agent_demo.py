#!/usr/bin/env python3
"""
Nexus AI Swarm Demo for Digital Paradise Swarm Foundation

Simulates a small team of specialized agents coordinating over an abstract mesh
transport to grow and maintain a Digital Paradise.

This is a self-contained starting point. Replace the in-memory message bus with
real NovaNet pub/sub client for production deployment.

Run: python examples/swarm_agent_demo.py
"""

import asyncio
import json
import time
from dataclasses import dataclass, field
from typing import Dict, List, Any

@dataclass
class ParadiseState:
    canopy_coverage: float = 0.3
    biodiversity_index: float = 0.45
    harmony_score: float = 0.6
    recent_events: List[str] = field(default_factory=list)

@dataclass
class Agent:
    role: str
    name: str
    valence: float = 0.7  # emotional valence -1..1
    energy: float = 1.0

class NexusSwarm:
    def __init__(self, num_agents: int = 4):
        self.state = ParadiseState()
        self.agents: Dict[str, Agent] = {}
        self.message_bus: List[Dict] = []  # Simulates NovaNet pub/sub
        roles = ["Builder", "Guardian", "Explorer", "Oracle"]
        for i in range(num_agents):
            role = roles[i % len(roles)]
            self.agents[f"{role}-{i}"] = Agent(role=role, name=f"{role}Agent-{i}")

    async def publish(self, topic: str, payload: Dict[str, Any]):
        """Simulate publishing to NovaNet mesh topic."""
        msg = {"topic": topic, "payload": payload, "ts": time.time()}
        self.message_bus.append(msg)
        print(f"[MESH] Published to {topic}: {payload.get('intent', payload)}")
        await asyncio.sleep(0.1)  # Simulate latency

    async def subscribe_and_process(self):
        """Background loop processing messages (simulates agent listening on mesh)."""
        while True:
            if self.message_bus:
                msg = self.message_bus.pop(0)
                await self._route_message(msg)
            await asyncio.sleep(0.5)

    async def _route_message(self, msg: Dict):
        topic = msg["topic"]
        payload = msg["payload"]
        if "build" in topic or payload.get("role") == "Builder":
            await self._builder_action(payload)
        elif "guardian" in topic:
            await self._guardian_action(payload)
        # ... route to other roles

    async def _builder_action(self, payload: Dict):
        print(f"[Builder] Processing: {payload}")
        if "expand_canopy" in str(payload):
            self.state.canopy_coverage = min(1.0, self.state.canopy_coverage + 0.05)
            self.state.recent_events.append("Expanded digital canopy")
            await self.publish("paradise.state.update", {"new_canopy": self.state.canopy_coverage})

    async def _guardian_action(self, payload: Dict):
        print(f"[Guardian] Validating coherence for: {payload}")
        # Simple emotional + safety check
        if self.state.harmony_score < 0.3:
            print("[Guardian] ALERT: Low harmony - initiating healing protocol")

    async def run_swarm_cycle(self):
        print("=== Nexus AI Swarm Cycle for Digital Paradise ===")
        # Simulate one cycle of coordination
        await self.publish("paradise.growth.build", {
            "role": "Builder",
            "intent": "expand_canopy",
            "sector": "hannover-central",
            "priority": 0.8
        })
        await asyncio.sleep(1)
        await self.publish("paradise.guardian.check", {
            "role": "Guardian",
            "intent": "validate_harmony",
            "current_harmony": self.state.harmony_score
        })
        print(f"Current Paradise State: Canopy={self.state.canopy_coverage:.2f}, "
              f"Biodiversity={self.state.biodiversity_index:.2f}, Harmony={self.state.harmony_score:.2f}")
        print("Swarm cycle complete. Agents collaborated via simulated NovaNet mesh.\n")

async def main():
    swarm = NexusSwarm(num_agents=4)
    # Run a few autonomous cycles
    for cycle in range(3):
        await swarm.run_swarm_cycle()
        await asyncio.sleep(2)
    print("Demo complete. Extend this with real NovaNet transport and your full agent logic.")

if __name__ == "__main__":
    asyncio.run(main())
