import copy
from typing import Dict


async def runtime(
    hub, name: str, ctx: Dict, seq: Dict, low: Dict, running: Dict, managed_state: Dict
):
    """
    Execute the runtime in parallel mode
    """
    inds = []
    for ind in seq:
        if seq[ind].get("unmet"):
            # Requisites are unmet, skip this one
            continue
        inds.append(ind)
    if not inds:
        # Nothing can be run, we have hit recursive requisite,
        # or we are done
        pass
    for ind in inds:
        await hub.idem.rules.init.run(
            name,
            copy.deepcopy(
                ctx
            ),  # every state run should use unique ctx so that ctx.acct retains correct information during whole state execution.
            low,
            seq[ind],
            running,
            hub.idem.RUNS[name]["run_num"],
            managed_state,
        )
        hub.idem.RUNS[name]["run_num"] += 1
