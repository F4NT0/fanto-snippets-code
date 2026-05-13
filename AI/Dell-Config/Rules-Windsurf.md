# Rules

The **rules/** directory contains AI guardrails and coding standards that guide Windsurf's AI behavior. 

These rules are automatically loaded and applied during AI-assisted development to ensureconsistency, security, and quality across the codebase.

## Files explanations

1. **branch-naming.md**

  - `Purpose:` Enforces Git branch naming conventions
  - `AI Use:` Guides AI to create properly named branches when suggesting Git operations
  - `Key Rules:` Uses prefixes like feat/, bug/, hotfix/; forbids protected tokens like main, prod, release
  - `Enforcement:` GitLab branch protection, code review checks

2. **coding-rules.md**

  - `Purpose:` Universal coding standards for .NET and React/TypeScript
  - `AI Use:` Ensures AI-generated code follows SOLID principles, clean architecture, proper async patterns, and type safety
  - `Key Rules:` SOLID principles, async/await best practices, functional React components, REST conventions
  - `Enforcement:` Linting, test gates, code review

3. **dds-react.md**

  - `Purpose:` Design system rules for DDS React components
  - `AI Use:` Activates when AI detects @dds/react usage, directing it to prefer design system components over custom implementations
  - `Key Rules:` Always consult DDS documentation first, prefer existing DDS components
  - `Trigger:` model_decision (context-aware activation)

4. **dead-code-rules.md**

  - `Purpose:` Mandates continuous cleanup of unused code
  - `AI Use:` Guides AI to remove dead code, unused imports, stale dependencies, and commented-out code during refactoring
  - `Key Rules:` Remove unused code/dependencies, clean up comments, safe removal process
  - `Enforcement:` Static analysis, build validation, code review

5. **linting-requirements.md**

  - `Purpose:` Enforces linting configuration standards
  - `AI Use:` Ensures AI uses the internal linting-configuration skill and maintains proper ESLint/Stylelint setups
  - `Key Rules:` Use internal linting skill, keep configs in-repo, required React tooling baseline
  - `Enforcement:` IDE integrations, pre-commit hooks, CI stages

6. **security-rules.md**

  - `Purpose:` Critical security standards and vulnerability scanning
  - `AI Use:` Forces AI to follow security best practices and run Snyk scans before merging
  - `Key Rules:` Defense-in-depth, input validation, secrets management, mandatory Snyk scans for code/dependencies/IaC
  - `Priority:` Critical (highest priority)
  - `Enforcement:` Pre-commit, CI security gates, security review

7. **testing-rules.md**

  - `Purpose:` Testing standards and coverage requirements
  - `AI Use:` Guides AI to write tests following Arrange-Act-Assert structure with proper coverage
  - `Key Rules:` 80% coverage (.NET), 70% coverage (React), xUnit/FluentAssertions for .NET, Jest/Vitest for React
  - `Enforcement:` Pre-commit, CI test gates, code review

8. **windsurf-requirements.md**

  - `Purpose:` Framework usage standards for Windsurf itself
  - `AI Use:` Ensures AI uses correct Windsurf workflows and skills, not submodule-based installation
  - `Key Rules:` Use internal skills (testing-setup, linting-configuration, security-review), required workflows (/setup-testing, /verify-and-commit), Snyk directive compliance
  - `Enforcement:` Project initialization, pre-commit validation, CI stages

## How AI Uses These Rules

When you interact with Windsurf's AI:

  1. `Context Loading`: Rules matching the current file types and context are automatically loaded
  2. `Behavior Guidance`: AI references these rules when generating code, suggesting refactors, or creating workflows
  3. `Validation`: AI checks its suggestions against these rules before presenting them
  4. `Workflow Integration`: Rules reference specific skills and workflows that AI should invoke

This creates a consistent, standards-compliant development experience where the AI acts as a knowledgeable team member who understands 
your organization's coding standards and security requirements.
