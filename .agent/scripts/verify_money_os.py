#!/usr/bin/env python3
"""
Ai Agent Money OS structural verifier.

Checks that the original automatic routing advantages remain present while the
Money OS business layer is installed.
"""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
AGENT = ROOT / ".agent"

EXPECTED_COUNTS = {
    "agents": 25,
    "skills": 67,
    "workflows": 16,
    "commands": 18,
    "claude_commands": 18,
}

REQUIRED_ENGINEERING_AGENTS = {
    "orchestrator.md",
    "project-planner.md",
    "frontend-specialist.md",
    "backend-specialist.md",
    "security-auditor.md",
    "debugger.md",
    "test-engineer.md",
}

REQUIRED_MONEY_AGENTS = {
    "01-offer-agent.md",
    "02-attraction-agent.md",
    "03-conversion-agent.md",
    "04-deliver-agent.md",
    "05-insights-agent.md",
}

REQUIRED_COMMANDS = {
    "research.md",
    "competitor.md",
    "offer.md",
    "funnel.md",
    "content.md",
    "lead-magnet.md",
    "sales-page.md",
    "copy.md",
    "objection.md",
    "payment-setup.md",
    "notification.md",
    "delivery.md",
    "landing-page.md",
    "payment-embed.md",
    "analytics.md",
    "revenue.md",
    "optimize.md",
}

REQUIRED_ROUTING_TERMS = {
    "security-auditor",
    "backend-specialist",
    "frontend-specialist",
    "debugger",
    "01-offer-agent",
    "02-attraction-agent",
    "03-conversion-agent",
    "04-deliver-agent",
    "05-insights-agent",
}


def fail(message: str) -> None:
    print(f"[FAIL] {message}")
    sys.exit(1)


def count_files(path: Path) -> int:
    return len([item for item in path.iterdir() if item.is_file()])


def count_dirs(path: Path) -> int:
    return len([item for item in path.iterdir() if item.is_dir()])


def assert_exists(path: Path, label: str) -> None:
    if not path.exists():
        fail(f"Missing {label}: {path}")


def main() -> None:
    assert_exists(AGENT, ".agent root")

    actual_counts = {
        "agents": count_files(AGENT / "agents"),
        "skills": count_dirs(AGENT / "skills"),
        "workflows": count_files(AGENT / "workflows"),
        "commands": count_files(AGENT / "commands"),
        "claude_commands": count_files(AGENT / ".claude" / "commands"),
    }

    for key, expected in EXPECTED_COUNTS.items():
        actual = actual_counts[key]
        if actual < expected:
            fail(f"{key} count too low: expected at least {expected}, got {actual}")

    agent_files = {item.name for item in (AGENT / "agents").iterdir() if item.is_file()}
    missing_engineering = REQUIRED_ENGINEERING_AGENTS - agent_files
    missing_money = REQUIRED_MONEY_AGENTS - agent_files
    if missing_engineering:
        fail(f"Missing original engineering agents: {sorted(missing_engineering)}")
    if missing_money:
        fail(f"Missing Money OS agents: {sorted(missing_money)}")

    command_files = {item.name for item in (AGENT / "commands").iterdir() if item.is_file()}
    missing_commands = REQUIRED_COMMANDS - command_files
    if missing_commands:
        fail(f"Missing Money OS commands: {sorted(missing_commands)}")

    routing = (AGENT / "skills" / "intelligent-routing" / "SKILL.md").read_text(encoding="utf-8")
    rules = (AGENT / "rules" / "GEMINI.md").read_text(encoding="utf-8")
    combined = f"{routing}\n{rules}"
    missing_terms = [term for term in REQUIRED_ROUTING_TERMS if term not in combined]
    if missing_terms:
        fail(f"Routing does not reference required agents: {missing_terms}")

    print("[OK] Ai Agent Money OS structure and automatic routing checks passed")
    for key, value in actual_counts.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
