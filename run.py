class Runner:
    @classmethod
    async def run(
        cls,
        starting_agent: Agent[TContext],
        input:str | list[TResponseInputItem],
        *,
        context:TContext | None = None,
        max_turns:int = DEFAULT_MAX_TURNS,



    )