#!/usr/bin/env python3
"""
Script to generate all placeholder files for Vonartis-Docs repository
"""

import os
from pathlib import Path

# Base directory
BASE_DIR = Path("/Users/fadiamiari/Documents/GitHub/Vonartis-Docs")

# Define all files to create with their paths
files_to_create = [
    # Current Products - remaining files
    "current-products/vonvault-identity/features.md",
    "current-products/vonvault-identity/benefits.md",
    "current-products/vonvault-identity/summary.md",
    "current-products/vonpay/overview.md",
    "current-products/vonpay/features.md",
    "current-products/vonpay/benefits.md",
    "current-products/vonpay/summary.md",
    "current-products/vonaio/overview.md",
    "current-products/vonaio/features.md",
    "current-products/vonaio/benefits.md",
    "current-products/vonaio/summary.md",
    "current-products/vonbit/overview.md",
    "current-products/vonbit/features.md",
    "current-products/vonbit/benefits.md",
    "current-products/vonbit/summary.md",
    
    # DragonFi - Executive Summary
    "dragonfi/executive-summary/big-picture.md",
    "dragonfi/executive-summary/problem.md",
    "dragonfi/executive-summary/solution.md",
    
    # DragonFi - Core Technologies
    "dragonfi/dyva.md",
    "dragonfi/ocme.md",
    "dragonfi/artis.md",
    "dragonfi/uea.md",
    
    # DragonFi - Tokenomics
    "dragonfi/tokenomics/why-three-tokens.md",
    "dragonfi/tokenomics/pbit.md",
    "dragonfi/tokenomics/cpbit.md",
    "dragonfi/tokenomics/fpbit.md",
    "dragonfi/tokenomics/distribution.md",
    
    # DragonFi - Roadmap
    "dragonfi/roadmap/phase-1.md",
    "dragonfi/roadmap/phase-2.md",
    "dragonfi/roadmap/phase-3.md",
    "dragonfi/roadmap/phase-4.md",
    "dragonfi/roadmap/phase-5.md",
    "dragonfi/roadmap/phase-6.md",
    "dragonfi/roadmap/phase-7.md",
    
    # DragonFi - Blockchain
    "dragonfi/blockchain/why-own-chain.md",
    "dragonfi/blockchain/proof-of-entropy.md",
    "dragonfi/blockchain/migration-strategy.md",
    
    # Technical Docs
    "technical-docs/hardware.md",
    "technical-docs/infrastructure.md",
    "technical-docs/applications.md",
    "technical-docs/security.md",
    "technical-docs/github.md",
    
    # For Investors
    "for-investors/opportunity.md",
    "for-investors/traction.md",
    "for-investors/competition.md",
    "for-investors/path-to-1b.md",
    "for-investors/team.md",
    "for-investors/the-ask.md",
    "for-investors/faq.md",
    
    # For Validators
    "for-validators/dyva-validator.md",
    "for-validators/ocme-agents.md",
    "for-validators/economics.md",
    
    # For Developers
    "for-developers/build-with-us.md",
    "for-developers/integration-guides.md",
    
    # Resources
    "resources/whitepaper.md",
    "resources/pitch-deck.md",
    "resources/media-pack.md",
    "resources/faq.md",
]

def create_file(file_path):
    """Create a markdown file with placeholder content"""
    full_path = BASE_DIR / file_path
    
    # Create directory if it doesn't exist
    full_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Get the title from the filename
    title = full_path.stem.replace("-", " ").title()
    
    # Create content
    content = f"# {title}\n\n*Coming soon*\n"
    
    # Write file
    with open(full_path, 'w') as f:
        f.write(content)
    
    print(f"Created: {file_path}")

def main():
    print(f"Creating {len(files_to_create)} files...")
    
    for file_path in files_to_create:
        create_file(file_path)
    
    print("\n✅ All files created successfully!")
    print(f"\nTotal files: {len(files_to_create)}")
    print(f"Location: {BASE_DIR}")

if __name__ == "__main__":
    main()
