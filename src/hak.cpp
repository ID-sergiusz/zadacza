#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k;
    if (!(cin >> k)) {
        return 0;
    }

    vector<vector<int>> target(k);
    int n = 0;

    for (int i = 0; i < k; ++i) {
        int c;
        cin >> c;
        target[i].resize(c);
        n += c;
        for (int &disk : target[i]) {
            cin >> disk;
        }
    }

    vector<int> rankOf(n + 1);
    vector<int> destination(n + 1);
    int rank = 0;
    for (int i = 0; i < k; ++i) {
        for (int disk : target[i]) {
            rankOf[disk] = rank++;
            destination[disk] = i;
        }
    }

    vector<deque<int>> towers(k);
    for (int i = 0; i < k; ++i) {
        int d;
        cin >> d;
        for (int j = 0; j < d; ++j) {
            int disk;
            cin >> disk;
            towers[i].push_back(disk);
        }
    }

    int bits = 0;
    while ((1 << bits) < n) {
        ++bits;
    }

    long long numberOfMoves = n - static_cast<int>(towers[0].size());
    numberOfMoves += 1LL * n * bits;
    numberOfMoves += n;
    for (int r = 0; r < n; ++r) {
        numberOfMoves += __builtin_popcount(static_cast<unsigned>(r));
    }

    cout << numberOfMoves << '\n';

    auto moveDisk = [&](int from, int to) {
        int disk = towers[from].front();
        towers[from].pop_front();
        towers[to].push_back(disk);
        cout << from + 1 << ' ' << to + 1 << '\n';
    };

    for (int i = 1; i < k; ++i) {
        while (!towers[i].empty()) {
            moveDisk(i, 0);
        }
    }

    for (int bit = 0; bit < bits; ++bit) {
        for (int j = 0; j < n; ++j) {
            int disk = towers[0].front();
            if ((rankOf[disk] >> bit) & 1) {
                moveDisk(0, 1);
            } else {
                moveDisk(0, 0);
            }
        }
        while (!towers[1].empty()) {
            moveDisk(1, 0);
        }
    }

    for (int j = 0; j < n; ++j) {
        int disk = towers[0].front();
        moveDisk(0, destination[disk]);
    }

    return 0;
}
