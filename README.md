# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--05_09:05:33_UTC-green)

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

**Latest saved flight:** 2026-04-05 09:05:33 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-05 09:05:33 UTC

- **17,584** saved flights
- **9,112** unique routes
- **114** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **17,584** saved routes in the archive
- **1h 16m** average flight duration

### Carbon Footprint Estimate

- **222,048.0 tonnes** estimated CO2 emissions
- **12,872,350 km** total distance flown
- **866 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 769 |
| 2 | Ryanair | 708 |
| 3 | IndiGo | 502 |
| 4 | EJA | 328 |
| 5 | American Airlines | 323 |
| 6 | Lufthansa | 248 |
| 7 | Southwest Airlines | 247 |
| 8 | ENY | 234 |
| 9 | Vueling | 198 |
| 10 | LATAM Airlines | 184 |
| 11 | AXM | 177 |
| 12 | All Nippon Airways | 156 |
| 13 | QLK | 153 |
| 14 | Delta Air Lines | 151 |
| 15 | LXJ | 149 |
| 16 | AZU | 131 |
| 17 | VIV | 131 |
| 18 | Swiss International | 129 |
| 19 | Alaska Airlines | 123 |
| 20 | Japan Airlines | 121 |
| 21 | United Airlines | 116 |
| 22 | easyJet | 114 |
| 23 | Avianca | 113 |
| 24 | AEE | 110 |
| 25 | EJU | 110 |
| 26 | AXB | 108 |
| 27 | EDV | 108 |
| 28 | WIF | 102 |
| 29 | BRC | 101 |
| 30 | Cathay Pacific | 101 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 13914 |
| 2 | 🇮🇳 IN | 1530 |
| 3 | 🇪🇸 ES | 1447 |
| 4 | 🇦🇺 AU | 1296 |
| 5 | 🇧🇷 BR | 1000 |
| 6 | 🇯🇵 JP | 960 |
| 7 | 🇩🇪 DE | 911 |
| 8 | 🇨🇴 CO | 905 |
| 9 | 🇮🇹 IT | 808 |
| 10 | 🇨🇦 CA | 780 |
| 11 | 🇬🇧 GB | 679 |
| 12 | 🇫🇷 FR | 634 |
| 13 | 🇲🇽 MX | 608 |
| 14 | 🇬🇷 GR | 488 |
| 15 | 🇨🇭 CH | 457 |
| 16 | 🇲🇾 MY | 402 |
| 17 | 🇳🇿 NZ | 394 |
| 18 | 🇿🇦 ZA | 369 |
| 19 | 🇵🇭 PH | 344 |
| 20 | 🇳🇴 NO | 341 |
| 21 | 🇬🇹 GT | 337 |
| 22 | 🇹🇷 TR | 325 |
| 23 | 🇰🇷 KR | 318 |
| 24 | 🇹🇭 TH | 248 |
| 25 | 🇵🇱 PL | 244 |
| 26 | 🇲🇦 MA | 213 |
| 27 | 🇮🇩 ID | 197 |
| 28 | 🇧🇸 BS | 191 |
| 29 | 🇲🇴 MO | 186 |
| 30 | 🇲🇪 ME | 182 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 420 |
| 2 | El Dorado International Airport |  | CO | 343 |
| 3 | Tokyo International Airport |  | JP | 329 |
| 4 | Denver International Airport |  | US | 327 |
| 5 | Indira Gandhi International Airport |  | IN | 318 |
| 6 | La Aurora Airport |  | GT | 237 |
| 7 | Harry Reid International Airport |  | US | 232 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 229 |
| 9 | Frankfurt am Main International Airport |  | DE | 220 |
| 10 | Zurich Airport |  | CH | 211 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 189 |
| 12 | Sydney Kingsford Smith International Airport |  | AU | 189 |
| 13 | Macau International Airport |  | MO | 186 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 182 |
| 15 | Guaymaral Airport |  | CO | 182 |
| 16 | Chicago O'Hare International Airport |  | US | 172 |
| 17 | Bengaluru International Airport |  | IN | 172 |
| 18 | Madrid Barajas International Airport |  | ES | 166 |
| 19 | Charlotte/Douglas International Airport |  | US | 165 |
| 20 | Atizapan De Zaragoza Airport |  | MX | 157 |
| 21 | Ninoy Aquino International Airport |  | PH | 157 |
| 22 | Congonhas Airport |  | BR | 154 |
| 23 | Tenerife Norte Airport |  | ES | 153 |
| 24 | Daniel K Inouye International Airport |  | US | 144 |
| 25 | Salt Lake City International Airport |  | US | 142 |
| 26 | Kuala Lumpur International Airport |  | MY | 142 |
| 27 | Netaji Subhash Chandra Bose International Airport |  | IN | 138 |
| 28 | Malpensa International Airport |  | IT | 137 |
| 29 | Reno/Tahoe International Airport |  | US | 136 |
| 30 | Vitoria/Foronda Airport |  | ES | 134 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 129 |
| 32 | Charles de Gaulle International Airport |  | FR | 128 |
| 33 | Miami International Airport |  | US | 123 |
| 34 | Barcelona International Airport |  | ES | 122 |
| 35 | Pune Airport |  | IN | 118 |
| 36 | George Bush Intcntl/Houston Airport |  | US | 117 |
| 37 | Seattle-Tacoma International Airport |  | US | 115 |
| 38 | John Paul II International Airport Kraków-Balice Airport |  | PL | 114 |
| 39 | General Edward Lawrence Logan International Airport |  | US | 112 |
| 40 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 110 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 83 | 1h 8m | 706 km | 1,010.5 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 79 | 14m | 114 km | 154.9 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 69 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 68 | 24m | 225 km | 263.8 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 62 | 29m | 304 km | 325.0 t |
| 6 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 53 | 27m | 152 km | 138.5 t |
| 7 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 52 | 1h 44m | 1,156 km | 1,037.4 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 52 | 31m | - | - |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 51 | 1h 27m | 910 km | 800.3 t |
| 10 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 49 | 16m | 206 km | 174.2 t |
| 11 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 46 | 22m | 99 km | 78.8 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 43 | 28m | 275 km | 203.8 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 40 | 19m | 165 km | 113.8 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 38 | 1h 11m | 770 km | 504.8 t |
| 15 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 38 | 1h 54m | 1,304 km | 854.9 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 37 | 30m | 369 km | 235.5 t |
| 17 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 37 | 52m | 556 km | 354.7 t |
| 18 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 36 | 54m | 546 km | 338.9 t |
| 19 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
| 20 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 33 | 1h 43m | 1,423 km | 809.9 t |
| 21 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 32 | 23m | 252 km | 138.9 t |
| 22 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 32 | 58m | 723 km | 398.9 t |
| 23 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 32 | 46m | 452 km | 249.4 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 30 | 13m | 99 km | 51.4 t |
| 25 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 30 | 11m | 127 km | 65.7 t |
| 26 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 30 | 9m | - | - |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 27 | 20m | 147 km | 68.3 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 26 | 1h 23m | 961 km | 431.0 t |
| 29 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 26 | 20m | 250 km | 112.3 t |
| 30 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 25 | 16m | 183 km | 78.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| HKC365 | HKC | London Stansted Airport (EGSS) | Zhuhai Airport (ZGSD) | 2026-04-04 21:07 UTC | 2026-04-05 09:05 UTC | 11h 57m |
| AFR188 | Air France | Charles de Gaulle International Airport (LFPG) | Zhuhai Airport (ZGSD) | 2026-04-04 21:50 UTC | 2026-04-05 09:02 UTC | 11h 11m |
| CPA2252 | Cathay Pacific | London Heathrow Airport (EGLL) | Zhuhai Airport (ZGSD) | 2026-04-04 21:34 UTC | 2026-04-05 08:57 UTC | 11h 22m |
| AXM6044 | AXM | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 2026-04-05 08:35 UTC | 2026-04-05 08:54 UTC | 18m |
| OKBIT | OKB | Letnany Airport (LKLT) | Medlanky Airport (LKCM) | 2026-04-05 07:54 UTC | 2026-04-05 08:53 UTC | 59m |
| FIN99 | Finnair | Helsinki Vantaa Airport (EFHK) | Macau International Airport (VMMC) | 2026-04-04 21:48 UTC | 2026-04-05 08:52 UTC | 11h 4m |
| RYR6AQ | Ryanair | Bergamo / Orio Al Serio Airport (LIME) | Tortoli' / Arbatax Airport (LIET) | 2026-04-05 08:03 UTC | 2026-04-05 08:51 UTC | 48m |
| CPA256 | Cathay Pacific | London Heathrow Airport (EGLL) | Macau International Airport (VMMC) | 2026-04-04 21:12 UTC | 2026-04-05 08:51 UTC | 11h 38m |
| SAZ51 | SAZ | Zurich Airport (LSZH) | Ikaria Airport (LGIK) | 2026-04-05 06:34 UTC | 2026-04-05 08:50 UTC | 2h 16m |
| N187QS |  | Westchester County Airport (KHPN) | Eleftherios Venizelos International Airport (LGAV) | 2026-04-05 00:40 UTC | 2026-04-05 08:49 UTC | 8h 9m |
| HLC260 | HLC | Osan Air Base (RKSO) | Osan Air Base (RKSO) | 2026-04-05 08:36 UTC | 2026-04-05 08:49 UTC | 12m |
| IXIAN | IXI | Mont-Dauphin - St-Crepin Airport (LFNC) | Mont-Dauphin - St-Crepin Airport (LFNC) | 2026-04-05 08:36 UTC | 2026-04-05 08:47 UTC | 11m |
| RYR67JA | Ryanair | London Stansted Airport (EGSS) | Tsalapita Airport (LB11) | 2026-04-05 06:13 UTC | 2026-04-05 08:46 UTC | 2h 33m |
| HKC393 | HKC | Budapest Ferenc Liszt International Airport (LHBP) | Macau International Airport (VMMC) | 2026-04-04 22:15 UTC | 2026-04-05 08:43 UTC | 10h 28m |
| AFR34UP | Air France | Charles de Gaulle International Airport (LFPG) | Václav Havel Airport (LKPR) | 2026-04-05 07:17 UTC | 2026-04-05 08:43 UTC | 1h 26m |
| PGT1863 | PGT | Ercan International Airport (LCEN) | Selcuk Efes Airport (LTFB) | 2026-04-05 07:49 UTC | 2026-04-05 08:41 UTC | 52m |
| SWR7AK | Swiss International | Nice-Cote d'Azur Airport (LFMN) | Zurich Airport (LSZH) | 2026-04-05 07:48 UTC | 2026-04-05 08:39 UTC | 51m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-04-05 07:50 UTC | 2026-04-05 08:39 UTC | 49m |
| HBZVU | HBZ | Muenster Aero Airport (LSPU) | Raron Airport (LSTA) | 2026-04-05 06:38 UTC | 2026-04-05 08:38 UTC | 2h 0m |
| SXS7EL | SXS | Trabzon International Airport (LTCG) | Karain Airport (LTXE) | 2026-04-05 05:01 UTC | 2026-04-05 08:37 UTC | 3h 36m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
