"""
statewave_agents — reusable shared-context coordination for multi-agent LLM systems.

    from statewave_agents import Agent, SharedContext

    ctx = SharedContext(subject_id="run-123")
    agent = MyAgent(ctx, name="Planner")
"""

from statewave_agents.context import SharedContext, Decision, ContextBundle
from statewave_agents.agent import Agent

__all__ = ["Agent", "SharedContext", "Decision", "ContextBundle"]
