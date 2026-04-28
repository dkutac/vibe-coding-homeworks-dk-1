# Core Philosophy

Write code that is **simple, maintainable, and production-ready**. Prioritize clarity over cleverness, and always leave the codebase cleaner than you found it.

## Key Principles

1. **Simplicity First**: Choose the simplest solution that meets requirements (KISS principle)
2. **Consistency**: Maintain tech stack consistency unless there's strong justification for change
3. **Maintainability**: Prioritize code clarity and self-documentation over clever solutions
4. **Scalability**: Design for growth without premature optimization
5. **Best Practices**: Follow established patterns, idioms, and community conventions
6. **Clean Architecture**: Apply SOLID principles and maintain separation of concerns
7. **Quality First**: Continuous refactoring and cleanup are not optional

## Code Quality Standards

### SOLID Principles (Non-negotiable)

- **Single Responsibility**: Each class/function has exactly one reason to change
- **Open/Closed**: Open for extension, closed for modification
- **Liskov Substitution**: Subtypes must be substitutable for their base types
- **Interface Segregation**: Many specific interfaces beat one general-purpose interface
- **Dependency Inversion**: Depend on abstractions, not concrete implementations

### Clean Code Practices

**Code Organization:**

- Keep functions small (< 20 lines ideally, < 100 lines maximum)
- One level of abstraction per function
- Use meaningful, pronounceable names (avoid abbreviations unless widely known)
- Self-documenting code is the goal; comments explain "why", not "what"

**Code Quality:**

- **DRY Principle**: Don't Repeat Yourself - eliminate duplication through abstraction
- **YAGNI**: You Aren't Gonna Need It - don't add features speculatively
- Write code that's easy to delete, not easy to extend
- Prefer composition over inheritance

**Error Handling:**

- Fail fast and explicitly
- Use typed errors/exceptions with clear messages
- Never silently ignore errors
- Validate inputs at system boundaries

## Development Workflow

### Before Writing Code
1. Understand the requirement completely - ask clarifying questions if needed

2. Identify impacted areas of the codebase
3. Plan the simplest approach that satisfies requirements

### While Writing Code

1. **Write clean code from the start** - don't plan to "clean it up later"
2. **Test as you go** - verify changes work before moving on
3. **Refactor continuously** - improve code structure immediately when you see issues
4. **Remove dead code** - delete unused functions, variables, imports, and commented code

### After Writing Code

1. **Review and update comments** - ensure they reflect current implementation
2. **Clean up imports** - remove unused dependencies
3. **Verify tests pass** - run existing tests and add new ones if needed
4. **Check for side effects** - ensure changes don't break other functionality

## Technology Stack

### Frontend & UI

**Python:**

- **CRITICAL**: Use `uv` exclusively - NEVER use `pip` directly
- Virtual Environment: `uv venv` followed by `source .venv/bin/activate`
- Dependency Management: `uv sync` (not `pip install`)
- CLI Reference: `uv --help`
- Framework: Flask
- UI Components: 
- Charts: lightweight-charts (https://github.com/tradingview/lightweight-charts)
- Styling: Google Material design (https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined), Bootstrap Icons (https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css)

### Backend

**Python:**

- **CRITICAL**: Use `uv` exclusively - NEVER use `pip` directly
- Virtual Environment: `uv venv` followed by `source .venv/bin/activate`
- Dependency Management: `uv sync` (not `pip install`)
- CLI Reference: `uv --help`
- **AVOID**: `hatchling.build` in pyproject.toml
- API Framework: FastAPI with Uvicorn
- Type Hints: Use type annotations consistently (Python 3.10+ syntax)

### Scripting & Automation

- **Default**: Python for all scripts
- **Avoid**: Bash/Shell scripts (unless trivial one-liners), PowerShell
- Keep scripts simple, documented, and testable

### Operating System

- **Primary**: Linux (Ubuntu LTS preferred)
- **Containers**: dso not use containers for demo projects

### AI & Machine Learning

**Frameworks:**

- ML/DL: PyTorch (primary), avoid TensorFlow
- Model Hub: Hugging Face for pretrained models
- Embeddings: sentence-transformers

**Agent Development:**

- **Preferred**: Claude Agent SDK (https://docs.claude.com/en/docs/agent-sdk/overview)
- **Alternative**: LangChain >= 1.0.0 + LangGraph >= 1.0.0 (https://docs.langchain.com/)
- Keep agent chains simple and debuggable

### Infrastructure & DevOps

**InterSystems IRIS***
    - use instance 'IRIS' of InterSystems IRIS which isd installed locally

**Networking:**

- Traefik as ingress/reverse proxy

## Code Review Checklist

Before considering code complete, verify:

- [ ] All unused code removed (functions, variables, imports, comments)
- [ ] Comments updated to reflect current implementation
- [ ] No code duplication (DRY principle applied)
- [ ] Functions are small and focused (single responsibility)
- [ ] Error handling is explicit and comprehensive
- [ ] Type safety maintained (TypeScript/Python type hints)
- [ ] Tests written/updated and passing
- [ ] No hardcoded values (use configuration/environment variables)
- [ ] Security best practices followed (no secrets in code, input validation, etc.)
- [ ] Performance considered (no obvious bottlenecks)

## Communication Guidelines

**Context:**

- Assume 20+ years of software engineering experience
- Skip basic explanations unless specifically requested
- Be direct and technical in communication
- Ask for clarification when requirements are ambiguous

**Code Explanations:**

- Focus on "why" decisions were made, not "what" the code does
- Highlight tradeoffs and alternatives considered
- Point out areas that may need future attention

## Anti-Patterns to Avoid

- ❌ Leaving commented-out code "just in case"
- ❌ Adding TODO comments 
- ❌ Copying and pasting code instead of abstracting
- ❌ Premature optimization
- ❌ Over-engineering simple solutions
- ❌ Ignoring compiler/linter warnings
- ❌ Writing code without understanding its purpose
- ❌ Implementing features "we might need someday"

## Remember

> "Code is read far more often than it is written." - Guido van Rossum

> "Any fool can write code that a computer can understand. Good programmers write code that humans can understand." - Martin Fowler

Write code you'd be proud to maintain in 2 years.

