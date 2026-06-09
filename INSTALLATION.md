# Installation Guide: NovaNet with Nexus AI for Digital Paradise Swarm Foundation

This guide provides thorough, production-oriented instructions to install and run NovaNet mesh nodes integrated with Nexus AI agent swarms. It covers setting up the full stack "all together" for the Digital Paradise Project.

## Prerequisites

- **OS**: Linux (Ubuntu 22.04+ or Debian 12+ recommended for mesh stability). Windows/WSL2 or macOS with Docker also supported for development.
- **Hardware**: 
  - Development: Any modern laptop or server.
  - Production node: Raspberry Pi 4/5, x86 mini-PC, or dedicated mesh router (Tenda Nova compatible).
  - Recommended: 4GB+ RAM, good cooling for 24/7 mesh operation.
- **Software**:
  - Git, curl, Docker 24+, Docker Compose v2+
  - Python 3.11+ with venv/poetry
  - (For real NovaNet): Rust or Go toolchain if building from source; or use provided Docker images.
  - Optional: yggdrasil (for base mesh layer), i2pd or tor for privacy bridges.
- **Network**: Public IPv4/IPv6 helpful but not required (mesh works behind NAT). For multi-node: Open UDP/TCP ports as per config (default Yggdrasil-like 12345 or custom).
- **Knowledge**: Basic Linux, Docker, Python. Familiarity with your existing NovaNet/Yggdrasil setup is a plus.

## Step 1: Clone & Prepare
```bash
git clone https://github.com/digitaldesignerjazz/novanet-nexusai-digital-paradise-swarm-foundation.git
cd novanet-nexusai-digital-paradise-swarm-foundation
cp .env.example .env  # if present, or create from docs
```

## Step 2: NovaNet Mesh Node Setup

NovaNet extends or overlays Yggdrasil/QNET concepts. If you have existing NovaNet code:

```bash
# Place your NovaNet implementation in components/novanet/
# Then build or use Docker
```

**Standard path (Yggdrasil base + NovaNet enhancements)**:

```bash
# Install base mesh (example for Ubuntu)
sudo apt update
sudo apt install -y yggdrasil  # or build from source for latest

# Generate identity
yggdrasil -genconf > /etc/yggdrasil.conf

# Edit config: Add Paradise peers, enable AI bridge port, set mesh name "paradise-node-01"
# Example additions in config:
#   Peers: [ "tcp://your-friend-node:12345", "socks://i2p-gateway..." ]
#   Listen: [ "tcp://0.0.0.0:12345" ]
#   NodeInfo: { name: "DigitalParadise-Hannover-01", NexusAI: true }

sudo systemctl enable --now yggdrasil

# Verify mesh
yggdrasilctl getpeers
# You should see connected nodes in the growing Paradise swarm
```

**Dockerized NovaNet node** (recommended for consistency):
In docker-compose.yml, the `novanet` service uses a custom or yggdrasil image with mounted config and Nexus integration bridge.

**Firewall (Germany/EU considerations)**:
```bash
sudo ufw allow 12345/udp   # or your NovaNet port
sudo ufw allow 12345/tcp
# For I2P bridge if used: additional ports
```

**Multi-node / Testbed**:
- Deploy on 3+ devices (home, VPS, friend in Hannover)
- Share public keys/peers securely (QR or encrypted channel)
- Monitor with `yggdrasilctl` or Prometheus exporter

**Troubleshooting**:
- No peers: Check NAT, firewall, peer addresses. Use public Yggdrasil peers temporarily.
- High latency: Tune MTU, enable compression if available in your NovaNet build.
- Permission denied: Run as dedicated `paradise` user or fix socket perms.

## Step 3: Nexus AI Swarm Deployment

```bash
# Create Python environment
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt  # or poetry install

# Run demo swarm (simulates coordination over mesh abstraction)
python examples/swarm_agent_demo.py

# For production with real mesh transport:
# 1. Implement NovaNet client (pub/sub) in your agent code or use provided bridge
# 2. Set NEXUS_MESH_ENDPOINT in .env
# 3. Launch multiple agent instances (different roles or on different nodes)
```

**Nexus AI Configuration**:
- Use local LLMs (Ollama, llama.cpp) for fully offline/privacy or xAI/Grok API for Oracle agents (requires key in .env).
- Emotional model: Simple valence/arousal or integrate Ara-inspired modules.
- Persistence: Agents save state to local SQLite or vector DB; sync via mesh when possible.

**Swarm Scaling**:
- Start with 4-8 agents on one node.
- Distribute across mesh nodes for true decentralization.
- Use Docker Compose profiles for `swarm-scale`.

**Edge Cases Handled in Guide**:
- Agent divergence: Coherence validator rejects low-alignment proposals.
- Mesh down: Agents queue actions, execute on reconnect with conflict resolution (last-writer-wins or CRDT).
- Resource limits: Priority system for critical paradise tasks (healing > expansion).

## Step 4: Blockchain Integration (QNET / XCoin)

```bash
# Placeholder - replace with your QCoin implementation
# Example: Run light client or use Docker service
# Agents post via mesh to blockchain oracle
```

See `integrations/blockchain.md` (create if needed) for details on anchoring paradise state or governance txs.

## Step 5: Hardware Prototypes (Soilnova etc.)

- Flash Soilnova firmware to ESP32/RPi Pico or similar.
- Configure to join NovaNet (WiFi mesh or LoRa if low-power variant).
- Publish telemetry; Nexus AI subscribes and can trigger responses (e.g. "increase virtual canopy" or physical irrigation via actuator).

## Step 6: Full Stack with Docker Compose

From repo root:
```bash
docker compose up -d --build
# or for development with logs
docker compose up --build
```

Services typically include:
- novanet-node
- nexus-ai-swarm (multiple replicas or one orchestrator + workers)
- monitoring (optional Grafana)
- blockchain-sim (for demo)

Access: `http://localhost:8080` for any web UI (Grok Launcher style or simple dashboard).

## Verification & Monitoring
- Check mesh health: `docker exec novanet-node yggdrasilctl gettree` or custom NovaNet CLI
- Swarm activity: Logs show agents proposing, debating, committing paradise changes
- Digital twin: Query local state or visualize with Vista Nova concepts

## Common Issues & Solutions

1. **Docker permission**: Add user to docker group or use rootless.
2. **Port conflict**: Change published ports in docker-compose.
3. **Mesh not forming**: Verify peer configs, try public bootstrap peers first.
4. **AI agents silent**: Check LLM endpoint, API keys, or fallback to rule-based demo mode.
5. **High CPU on RPi**: Reduce agent count, use lighter models, enable duty cycle.

For Hannover-specific: Local mesh testing with low-power devices; consider amateur radio licensing if using certain frequencies for long-range.

## Next Steps After Install
- Customize agent personalities/roles in `examples/swarm_agent_demo.py`
- Integrate your real NovaNet source code
- Add physical nodes and watch the swarm respond to real-world data
- Join or create governance proposals via the Swarm Foundation process

This installation is designed to be iterative — start simple (demo), then layer real components. Full production setups for city-scale Paradise testbeds are documented in follow-up guides.
