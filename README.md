# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--03_16:48:24_UTC-green)

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

**Latest saved flight:** 2026-04-03 16:48:24 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-03 16:48:24 UTC

- **13,722** saved flights
- **7,625** unique routes
- **112** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **13,722** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **170,301.2 tonnes** estimated CO2 emissions
- **9,872,535 km** total distance flown
- **855 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 571 |
| 2 | Ryanair | 527 |
| 3 | IndiGo | 396 |
| 4 | EJA | 269 |
| 5 | American Airlines | 243 |
| 6 | Lufthansa | 208 |
| 7 | Southwest Airlines | 192 |
| 8 | ENY | 176 |
| 9 | Vueling | 147 |
| 10 | LATAM Airlines | 143 |
| 11 | AXM | 142 |
| 12 | All Nippon Airways | 123 |
| 13 | QLK | 123 |
| 14 | LXJ | 122 |
| 15 | Swiss International | 106 |
| 16 | Delta Air Lines | 105 |
| 17 | AZU | 103 |
| 18 | VIV | 100 |
| 19 | WIF | 97 |
| 20 | Japan Airlines | 89 |
| 21 | AXB | 88 |
| 22 | Alaska Airlines | 87 |
| 23 | Cathay Pacific | 85 |
| 24 | easyJet | 85 |
| 25 | United Airlines | 85 |
| 26 | EJU | 83 |
| 27 | EDV | 82 |
| 28 | AEE | 81 |
| 29 | GLO | 81 |
| 30 | BRC | 75 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 10824 |
| 2 | 🇮🇳 IN | 1206 |
| 3 | 🇦🇺 AU | 1082 |
| 4 | 🇪🇸 ES | 1058 |
| 5 | 🇧🇷 BR | 797 |
| 6 | 🇩🇪 DE | 742 |
| 7 | 🇯🇵 JP | 727 |
| 8 | 🇨🇴 CO | 642 |
| 9 | 🇨🇦 CA | 634 |
| 10 | 🇮🇹 IT | 603 |
| 11 | 🇬🇧 GB | 529 |
| 12 | 🇲🇽 MX | 481 |
| 13 | 🇫🇷 FR | 474 |
| 14 | 🇬🇷 GR | 370 |
| 15 | 🇨🇭 CH | 360 |
| 16 | 🇳🇿 NZ | 325 |
| 17 | 🇲🇾 MY | 319 |
| 18 | 🇳🇴 NO | 313 |
| 19 | 🇿🇦 ZA | 289 |
| 20 | 🇵🇭 PH | 265 |
| 21 | 🇹🇷 TR | 255 |
| 22 | 🇬🇹 GT | 252 |
| 23 | 🇰🇷 KR | 237 |
| 24 | 🇵🇱 PL | 193 |
| 25 | 🇹🇭 TH | 186 |
| 26 | 🇮🇩 ID | 166 |
| 27 | 🇲🇦 MA | 163 |
| 28 | 🇲🇴 MO | 157 |
| 29 | 🇧🇸 BS | 143 |
| 30 | 🇲🇪 ME | 143 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 329 |
| 2 | Indira Gandhi International Airport |  | IN | 255 |
| 3 | Tokyo International Airport |  | JP | 253 |
| 4 | Denver International Airport |  | US | 239 |
| 5 | El Dorado International Airport |  | CO | 227 |
| 6 | Frankfurt am Main International Airport |  | DE | 196 |
| 7 | Harry Reid International Airport |  | US | 186 |
| 8 | La Aurora Airport |  | GT | 175 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 171 |
| 10 | Zurich Airport |  | CH | 166 |
| 11 | Sydney Kingsford Smith International Airport |  | AU | 159 |
| 12 | Macau International Airport |  | MO | 157 |
| 13 | Guaymaral Airport |  | CO | 155 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 149 |
| 15 | Bengaluru International Airport |  | IN | 135 |
| 16 | Hartsfield/Jackson Atlanta International Airport |  | US | 129 |
| 17 | Chicago O'Hare International Airport |  | US | 129 |
| 18 | Congonhas Airport |  | BR | 126 |
| 19 | Atizapan De Zaragoza Airport |  | MX | 121 |
| 20 | Ninoy Aquino International Airport |  | PH | 121 |
| 21 | Charlotte/Douglas International Airport |  | US | 120 |
| 22 | Madrid Barajas International Airport |  | ES | 119 |
| 23 | Kuala Lumpur International Airport |  | MY | 117 |
| 24 | Tenerife Norte Airport |  | ES | 112 |
| 25 | Netaji Subhash Chandra Bose International Airport |  | IN | 109 |
| 26 | Vitoria/Foronda Airport |  | ES | 103 |
| 27 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 101 |
| 28 | Salt Lake City International Airport |  | US | 101 |
| 29 | Charles de Gaulle International Airport |  | FR | 100 |
| 30 | Reno/Tahoe International Airport |  | US | 99 |
| 31 | Malpensa International Airport |  | IT | 98 |
| 32 | Daniel K Inouye International Airport |  | US | 97 |
| 33 | Barcelona International Airport |  | ES | 95 |
| 34 | Pune Airport |  | IN | 93 |
| 35 | Austin-Bergstrom International Airport |  | US | 88 |
| 36 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 87 |
| 37 | Gimpo International Airport |  | KR | 86 |
| 38 | Seattle-Tacoma International Airport |  | US | 86 |
| 39 | Amsterdam Airport Schiphol |  | NL | 85 |
| 40 | General Edward Lawrence Logan International Airport |  | US | 84 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 62 | 14m | 114 km | 121.6 t |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 61 | 1h 7m | 706 km | 742.7 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 60 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 51 | 24m | 225 km | 197.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 46 | 29m | 304 km | 241.1 t |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 42 | 1h 46m | 1,156 km | 837.9 t |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 41 | 31m | - | - |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 36 | 1h 26m | 910 km | 564.9 t |
| 9 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
| 10 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 35 | 22m | 99 km | 60.0 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 34 | 20m | 165 km | 96.7 t |
| 12 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 33 | 26m | 152 km | 86.2 t |
| 13 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 32 | 15m | 206 km | 113.8 t |
| 14 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 32 | 28m | 275 km | 151.6 t |
| 15 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 31 | 53m | 546 km | 291.9 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 30 | 30m | 369 km | 191.0 t |
| 17 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 30 | 53m | 556 km | 287.6 t |
| 18 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 28 | 1h 55m | 1,304 km | 629.9 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 27 | 1h 43m | 1,423 km | 662.6 t |
| 20 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 27 | 1h 10m | 770 km | 358.7 t |
| 21 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 25 | 20m | 147 km | 63.3 t |
| 22 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 25 | 9m | - | - |
| 23 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 24 | 23m | 252 km | 104.2 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 24 | 11m | 127 km | 52.5 t |
| 25 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 23 | 1h 0m | 723 km | 286.7 t |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 22 | 44m | 452 km | 171.5 t |
| 27 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 22 | 13m | 99 km | 37.7 t |
| 28 | Auckland International Airport (NZAA) | Omarama Glider Airport (NZOA) | 19 | 1h 16m | 924 km | 303.0 t |
| 29 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 19 | 17m | 183 km | 59.9 t |
| 30 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 19 | 32m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N734VQ |  | Orlando Executive Airport (KORL) | Orlando Executive Airport (KORL) | 2026-04-03 16:36 UTC | 2026-04-03 16:48 UTC | 11m |
| PFA256 | PFA | Vero Beach Regional Airport (KVRB) | Hilton Head Airport (KHXD) | 2026-04-03 14:48 UTC | 2026-04-03 16:45 UTC | 1h 57m |
| ROU2074 | ROU | Vancouver International Airport (CYVR) | Warburg / Zajes Airport (CFH8) | 2026-04-03 15:07 UTC | 2026-04-03 16:26 UTC | 1h 18m |
| AXEL10 | AXE | Biggs Army Air Field (Fort Bliss) Airport (KBIF) | Hereford Municipal Airport (KHRX) | 2026-04-03 15:03 UTC | 2026-04-03 16:26 UTC | 1h 22m |
| N123KS |  | Lakeland Linder International Airport (KLAL) | Bartow Executive Airport (KBOW) | 2026-04-03 16:13 UTC | 2026-04-03 16:21 UTC | 8m |
| N6776A |  | Coyote Run Airport (0ID3) | Dogs Run Free Airport (WA76) | 2026-04-03 14:14 UTC | 2026-04-03 16:16 UTC | 2h 1m |
| JTZ623 | JTZ | Destin Executive Airport (KDTS) | Calhoun County Airport (K04M) | 2026-04-03 15:34 UTC | 2026-04-03 16:13 UTC | 38m |
| N601PF |  | KS67 (KS67) | Glenns Ferry Municipal Airport (KU89) | 2026-04-03 15:58 UTC | 2026-04-03 16:13 UTC | 14m |
| N616NE |  | Ryan Aerodrome (7TX7) | 5TA6 (5TA6) | 2026-04-03 15:53 UTC | 2026-04-03 16:12 UTC | 19m |
| CGTFK | CGT | Edmonton / Villeneuve Airport (CZVL) | Edmonton / Villeneuve Airport (CZVL) | 2026-04-03 15:28 UTC | 2026-04-03 16:12 UTC | 43m |
| N69FR |  | Philadelphia International Airport (KPHL) | Green Bank Observatory Airport (WV52) | 2026-04-03 15:29 UTC | 2026-04-03 16:11 UTC | 42m |
| OXF6039 | OXF | Falcon Field (KFFZ) | Montezuma Airport (19AZ) | 2026-04-03 15:35 UTC | 2026-04-03 16:11 UTC | 35m |
| SPALP | SPA | Pobiednik Wielki Airport (EPKP) | Pobiednik Wielki Airport (EPKP) | 2026-04-03 15:31 UTC | 2026-04-03 16:09 UTC | 38m |
| WZZ522 | Wizz Air | Mollis Airport (LSZM) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-04-03 14:28 UTC | 2026-04-03 16:09 UTC | 1h 40m |
| CHX3 | CHX | Meinerzhagen Airport (EDKZ) | Bonn-Hangelar Airport (EDKB) | 2026-04-03 15:50 UTC | 2026-04-03 16:07 UTC | 17m |
| ASP869 | ASP | Toronto Pearson International Airport (CYYZ) | Lehigh Valley International Airport (KABE) | 2026-04-03 15:12 UTC | 2026-04-03 16:05 UTC | 52m |
| EXS73BU | EXS | London Stansted Airport (EGSS) | Cardak Airport (LTAY) | 2026-04-03 12:40 UTC | 2026-04-03 16:05 UTC | 3h 24m |
| TGOZI | TGO | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 2026-04-03 15:37 UTC | 2026-04-03 16:04 UTC | 27m |
| AAL3044 | American Airlines | Philadelphia International Airport (KPHL) | General Edward Lawrence Logan International Airport (KBOS) | 2026-04-03 15:13 UTC | 2026-04-03 16:03 UTC | 50m |
| N496SP |  | Dupage Airport (KDPA) | Dupage Airport (KDPA) | 2026-04-03 15:56 UTC | 2026-04-03 16:03 UTC | 7m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
