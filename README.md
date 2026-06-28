# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--28_15:47:24_UTC-green)

![Flight Map](images/flight_map.png)

## About

Historical archive of saved air traffic routes collected from the [OpenSky Network](https://opensky-network.org/) API. This repository keeps appending completed flights to `data/flights/` and rebuilds the visuals from the full archive.

**Data Source:** Saved route files in `data/flights/` (originally fetched from OpenSky `/flights/all`)

**Update Frequency:** Every 5 minutes via GitHub Actions

**How it works:**
- Fetches recently completed routes from OpenSky
- Saves each route as a JSON file in `data/flights/`
- Rebuilds aggregate statistics from all saved historical routes
- Generates a historical route map and archive summary
- Generates daily reports, weekly leaderboards, and timelapse GIFs

## Route Timelapse

![Timelapse](images/timelapse.gif)

## Archive Snapshot

**Latest saved flight:** 2026-06-28 15:47:24 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-28 15:47:24 UTC

- **122,656** saved flights
- **42,072** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **122,656** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,483,271.6 tonnes** estimated CO2 emissions
- **85,986,759 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5029 |
| 2 | SkyWest Airlines | 4524 |
| 3 | EJA | 2370 |
| 4 | IndiGo | 2354 |
| 5 | American Airlines | 1891 |
| 6 | Southwest Airlines | 1835 |
| 7 | ENY | 1534 |
| 8 | Delta Air Lines | 1452 |
| 9 | Lufthansa | 1325 |
| 10 | LATAM Airlines | 1099 |
| 11 | Vueling | 1093 |
| 12 | WIF | 1085 |
| 13 | AZU | 1030 |
| 14 | AXM | 988 |
| 15 | LXJ | 933 |
| 16 | Swiss International | 858 |
| 17 | All Nippon Airways | 832 |
| 18 | Alaska Airlines | 803 |
| 19 | easyJet | 786 |
| 20 | QLK | 778 |
| 21 | EJU | 769 |
| 22 | Cathay Pacific | 687 |
| 23 | AEE | 679 |
| 24 | Air France | 671 |
| 25 | VIV | 667 |
| 26 | United Airlines | 659 |
| 27 | CXK | 650 |
| 28 | MXY | 639 |
| 29 | JetBlue | 616 |
| 30 | AXB | 610 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 104118 |
| 2 | 🇪🇸 ES | 8271 |
| 3 | 🇮🇳 IN | 7386 |
| 4 | 🇦🇺 AU | 7181 |
| 5 | 🇧🇷 BR | 6786 |
| 6 | 🇩🇪 DE | 6535 |
| 7 | 🇮🇹 IT | 6531 |
| 8 | 🇨🇦 CA | 6449 |
| 9 | 🇯🇵 JP | 5427 |
| 10 | 🇬🇧 GB | 5408 |
| 11 | 🇫🇷 FR | 4884 |
| 12 | 🇨🇴 CO | 4027 |
| 13 | 🇲🇽 MX | 3569 |
| 14 | 🇬🇷 GR | 3503 |
| 15 | 🇳🇴 NO | 3381 |
| 16 | 🇨🇭 CH | 3153 |
| 17 | 🇹🇷 TR | 2557 |
| 18 | 🇲🇾 MY | 2557 |
| 19 | 🇿🇦 ZA | 2041 |
| 20 | 🇵🇱 PL | 2019 |
| 21 | 🇳🇿 NZ | 1986 |
| 22 | 🇹🇭 TH | 1932 |
| 23 | 🇰🇷 KR | 1926 |
| 24 | 🇵🇭 PH | 1758 |
| 25 | 🇬🇹 GT | 1700 |
| 26 | 🇲🇦 MA | 1313 |
| 27 | 🇲🇪 ME | 1222 |
| 28 | 🇲🇴 MO | 1176 |
| 29 | 🇳🇱 NL | 1171 |
| 30 | 🇧🇸 BS | 1062 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2574 |
| 2 | Denver International Airport |  | US | 2056 |
| 3 | Tokyo International Airport |  | JP | 1797 |
| 4 | Indira Gandhi International Airport |  | IN | 1627 |
| 5 | Harry Reid International Airport |  | US | 1527 |
| 6 | Guaymaral Airport |  | CO | 1517 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1479 |
| 8 | Zurich Airport |  | CH | 1357 |
| 9 | La Aurora Airport |  | GT | 1313 |
| 10 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1301 |
| 11 | Frankfurt am Main International Airport |  | DE | 1279 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1203 |
| 13 | Chicago O'Hare International Airport |  | US | 1188 |
| 14 | Macau International Airport |  | MO | 1176 |
| 15 | El Dorado International Airport |  | CO | 1171 |
| 16 | Salt Lake City International Airport |  | US | 1064 |
| 17 | Capua Airport |  | IT | 1050 |
| 18 | Madrid Barajas International Airport |  | ES | 1021 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1020 |
| 20 | Kuala Lumpur International Airport |  | MY | 993 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 967 |
| 22 | Congonhas Airport |  | BR | 952 |
| 23 | Charlotte/Douglas International Airport |  | US | 924 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 905 |
| 25 | Charles de Gaulle International Airport |  | FR | 898 |
| 26 | Bengaluru International Airport |  | IN | 888 |
| 27 | Malpensa International Airport |  | IT | 853 |
| 28 | Ninoy Aquino International Airport |  | PH | 815 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 803 |
| 30 | Daniel K Inouye International Airport |  | US | 785 |
| 31 | Barcelona International Airport |  | ES | 769 |
| 32 | Tenerife Norte Airport |  | ES | 763 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 748 |
| 34 | Calgary International Airport |  | CA | 718 |
| 35 | Vitoria/Foronda Airport |  | ES | 713 |
| 36 | Amsterdam Airport Schiphol |  | NL | 708 |
| 37 | Norman Y Mineta San Jose International Airport |  | US | 707 |
| 38 | Scottsdale Airport |  | US | 705 |
| 39 | Seattle-Tacoma International Airport |  | US | 702 |
| 40 | Don Mueang International Airport |  | TH | 698 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 632 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 445 | 21m | 244 km | 1,873.8 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 320 | 24m | 225 km | 1,241.4 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 310 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 296 | 1h 10m | 770 km | 3,932.1 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 294 | 1h 25m | 910 km | 4,613.5 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 240 | 26m | 275 km | 1,137.3 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 231 | 31m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 178 | 22m | 55 km | 169.2 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 177 | 26m | 215 km | 655.5 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 174 | 20m | 99 km | 298.0 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 170 | 13m | - | - |
| 17 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 168 | 44m | 241 km | 697.8 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 167 | 27m | 152 km | 436.4 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 158 | 31m | 369 km | 1,005.7 t |
| 20 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 157 | 1h 44m | 1,423 km | 3,853.0 t |
| 21 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 155 | 44m | 452 km | 1,208.0 t |
| 22 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 154 | 18m | 144 km | 383.1 t |
| 24 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 151 | 20m | 250 km | 652.2 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 144 | 1h 38m | 1,156 km | 2,872.7 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 141 | 1h 1m | 695 km | 1,690.2 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 139 | 1h 17m | 961 km | 2,304.0 t |
| 28 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 137 | 29m | 49 km | 115.8 t |
| 29 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 137 | 13m | - | - |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 135 | 20m | 147 km | 341.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N6538F |  | Lakeland Linder International Airport (KLAL) | South Lakeland Airport (KX49) | 2026-06-28 14:49 UTC | 2026-06-28 15:47 UTC | 57m |
| N59FM |  | Tucson International Airport (KTUS) | Four Pillars Airport (AZ21) | 2026-06-28 15:11 UTC | 2026-06-28 15:41 UTC | 30m |
| DLH1YF | Lufthansa | Gerstetten Airport (EDPT) | Stuttgart Airport (EDDS) | 2026-06-28 14:31 UTC | 2026-06-28 15:39 UTC | 1h 7m |
| N690SG |  | Grand Junction Regional Airport (KGJT) | Blanding Municipal Airport (KBDG) | 2026-06-28 15:02 UTC | 2026-06-28 15:37 UTC | 34m |
| ATG9720 | ATG | Ben Gurion International Airport (LLBG) | Zhuhai Airport (ZGSD) | 2026-06-28 05:45 UTC | 2026-06-28 15:31 UTC | 9h 46m |
| XABEG | XAB | General Mariano Escobedo International Airport (MMMY) | Laredo International Airport (KLRD) | 2026-06-28 14:58 UTC | 2026-06-28 15:30 UTC | 31m |
| N135RF |  | Casas Adobes Airpark (NM69) | Casas Adobes Airpark (NM69) | 2026-06-28 15:16 UTC | 2026-06-28 15:29 UTC | 12m |
| THY6256 | Turkish Airlines | Istanbul Airport (LTFM) | Zhuhai Airport (ZGSD) | 2026-06-28 01:16 UTC | 2026-06-28 15:27 UTC | 14h 11m |
| N78AS |  | Pueblo Memorial Airport (KPUB) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-06-28 14:58 UTC | 2026-06-28 15:26 UTC | 28m |
| N818TH |  | Nice-Cote d'Azur Airport (LFMN) | Bangor International Airport (KBGR) | 2026-06-28 07:47 UTC | 2026-06-28 15:23 UTC | 7h 36m |
| N106RF |  | Las Cruces International Airport (KLRU) | Adobe Ranch Private Airport (NM37) | 2026-06-28 14:33 UTC | 2026-06-28 15:22 UTC | 49m |
| N336MA |  | Orlando Apopka Airport (KX04) | Orlando Apopka Airport (KX04) | 2026-06-28 14:22 UTC | 2026-06-28 15:20 UTC | 58m |
| EPI322 | EPI | New Smyrna Beach Municipal (Jack Bolt Field) Airport (KEVB) | North Exuma Airport (85FA) | 2026-06-28 14:50 UTC | 2026-06-28 15:20 UTC | 30m |
| FHHPS | FHH | Ajaccio-Napoleon Bonaparte Airport (LFKJ) | Corte Airport (LFKT) | 2026-06-28 15:01 UTC | 2026-06-28 15:17 UTC | 16m |
| N803ME |  | Knox County Regional Airport (KRKD) | Knox County Regional Airport (KRKD) | 2026-06-28 15:16 UTC | 2026-06-28 15:17 UTC | 1m |
| N53371 |  | Palm Beach County Park Airport (KLNA) | Palm Beach County Park Airport (KLNA) | 2026-06-28 14:35 UTC | 2026-06-28 15:17 UTC | 42m |
| SCA35 | SCA | Scottsdale Airport (KSDL) | Montezuma Airport (19AZ) | 2026-06-28 14:46 UTC | 2026-06-28 15:17 UTC | 30m |
| DFSCM | DFS | Munster-Telgte Airport (EDLT) | Munster-Telgte Airport (EDLT) | 2026-06-28 13:56 UTC | 2026-06-28 15:15 UTC | 1h 19m |
| N2112K |  | Erie Municipal Airport (KEIK) | Erie Municipal Airport (KEIK) | 2026-06-28 14:11 UTC | 2026-06-28 15:14 UTC | 1h 2m |
| N235ND |  | Erie Municipal Airport (KEIK) | Erie Municipal Airport (KEIK) | 2026-06-28 15:09 UTC | 2026-06-28 15:13 UTC | 4m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
