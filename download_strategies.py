#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Strategies de telechargement yt-dlp partagees entre youtube_downloader.py
(interface graphique) et download_batch.py (CLI en lot).
"""

STRATEGIES = [
    {
        'name': 'Client Android Music (Optimisé pour audio)',
        'args': [
            '--extractor-args', 'youtube:player_client=android_music',
            '--no-check-certificates',
        ]
    },
    {
        'name': 'Client Web Mobile (Sans JS challenges)',
        'args': [
            '--extractor-args', 'youtube:player_client=mweb',
            '--no-check-certificates',
        ]
    },
    {
        'name': 'Cookies Firefox + Client Android',
        'args': [
            '--cookies-from-browser', 'firefox',
            '--extractor-args', 'youtube:player_client=android_music',
            '--no-check-certificates',
        ]
    },
    {
        'name': 'Client Android Embedded',
        'args': [
            '--extractor-args', 'youtube:player_client=android_embedded',
            '--no-check-certificates',
        ]
    },
    {
        'name': 'Cookies Firefox + Client Web',
        'args': [
            '--remote-components', 'ejs:github',
            '--cookies-from-browser', 'firefox',
            '--no-check-certificates',
        ]
    },
    {
        'name': 'Client iOS (Audio quality)',
        'args': [
            '--extractor-args', 'youtube:player_client=ios',
            '--no-check-certificates',
            '--user-agent', 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15',
        ]
    },
    {
        'name': 'Mode basique multi-clients',
        'args': [
            '--extractor-args', 'youtube:player_client=android,web',
            '--no-check-certificates',
        ]
    },
    {
        'name': 'Mode legacy (Dernier recours)',
        'args': [
            '--no-check-certificates',
            '--extractor-args', 'youtube:skip=dash,hls',
        ]
    }
]
