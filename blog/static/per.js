/** This code was written in jest when I was new to web dev
**  Definitely not my best piece of work! 
*/

var ItemView = Backbone.View.extend({

    tagName: "td",

    events: {
        "click": "updateUnionIds"
    },

    initialize: function() {
        this.model.on("change", this.update, this);
    },

    update: function() {
        var status = this.model.get("status");
        this.$el.attr("class", status);
    },

    render: function() {
        var position = this.model.get("position");  
        this.$el.html(position);
        this.update();
        this.options.parent.append(this.$el);
    },

    updateUnionIds: function() {
        this.model.unblock();
        window.tableView.setAllUnionIds();
        return this;
    },

    setUnionId: function(id) {
        this.$el.html(id);
        return this;
    }
});

var TableView = Backbone.View.extend({
    el: "#table-parent",

    initialize: function(options) {
        this.options = options;
        this.items = [];
        this.size = this.options.size;
        this.model.on("change:percolated", this.update, this);
    },
    
    render: function() {
        var table= $("<table>");
        for(var i=0; i<this.size; i++) {
            var row = $("<tr>");
            for(var j=0; j<this.size; j++) {
                var item = new ItemView({
                    model: this.model.items[(i)*this.size + j + 1],
                    parent: row
                });
                this.items.push(item)
                item.render();
                
            }
            table.append(row);
        }
        this.$el.append(table)

        $(".initial-hidden").css("visibility", "visible");
        return this;
    },

    update: function() {
        var unblockedCount = this.model.get("unblockedCount");
        $("#message").html("Explored: " + unblockedCount)
    },

    setAllUnionIds: function() {
        for(var i = 0; i < this.size*this.size; i++) {
            var item = this.items[i];
            var position = item.model.get("position");
            var id = window.unionFind.unionIds[position];
            var rootId = window.unionFind.root(id);
            item.setUnionId(rootId);
        }
    },

    reset: function() {
        this.setAllUnionIds();
        return this;
    }
});

var UnionFind = function(count) {
    this.unionIds = new Array(count);
    this.rootSizes = new Array(count);
    for(var i=0; i<this.unionIds.length; i++) {
        this.unionIds[i] = i;
        this.rootSizes[i] = 1;
    }

};

UnionFind.prototype.find = function(one, two) {
    return this.root(one) === this.root(two);
};

UnionFind.prototype.root = function(position) {
    var up = this.unionIds[position];
    while(up != this.unionIds[up]) {
        up = this.unionIds[up];
    }
    return up;
};

UnionFind.prototype.union = function(one, two) {
    var rootOne = this.root(one);
    var rootTwo = this.root(two);
    if(rootOne === rootTwo) {
        return rootOne;
    }
    if(this.rootSizes[rootOne] >= this.rootSizes[rootTwo]) {
        this.unionIds[rootTwo] = rootOne;
        this.rootSizes[rootOne] += this.rootSizes[rootTwo]
    }
    else {
        this.unionIds[rootOne] = rootTwo
        this.rootSizes[rootTwo] += this.rootSizes[rootOne]

    }
    return this.unionIds[rootOne];

}

_.extend(UnionFind.prototype, Backbone.Events);

var PercolationItem = Backbone.Model.extend({

    defaults: {
        unionId: 1
    },

    unblock: function() {
        this.get("parent").unblockItem(this.get("position"));
    }
});

var Percolation = Backbone.Model.extend({
    defaults: {
        percolated: false,
        unblockedCount: 0
    },

    initialize: function() {
        var size = this.get("size");
        this.total = size * size + 2;
        this.top = 0;
        this.bottom = this.total - 1;
        this.size = size;

        this.resetUnionFind();
        this.items = {};
        for(var i=0; i<this.total; i++) {
            var item = new PercolationItem({
                position: i, 
                status: "blocked",
                parent: this
            });
            this.items[i] = item;
        }
        this.resetItems();

    },

    resetUnionFind: function() {
        this.unionFind = new UnionFind(this.total);
        window.unionFind = this.unionFind;
        this.set(this.defaults);
        return this;
    },

    resetItems: function() {
        _.each(this.items, function(item) {
            item.set("status", "blocked");
        });
        this.items[this.top].set("status", "percolated");
        this.items[this.bottom].set("status", "unblocked");
        return this;
    },

    unblockItem: function(position) {
        if(this.items[position].get("status") !== "blocked") {
            return;
        }

        var neighbours = this.getNeighbours(position);
        for(var i=0; i<neighbours.length; i++) {
            var neighbour = neighbours[i];
            if(this.items[neighbour].get("status") !== "blocked") {
                this.unionFind.union(position, neighbour);
            }
        }
        var status;
        if(this.isConnected(this.top, position)) {
            status = "percolated";
        }
        else {
            status = "unblocked";
        }
        this.items[position].set("status", status);

        var self = this;
        var percolateNeighboursRecursively = function(position) {
            var neighbours = self.getNeighbours(position);
            for(var i=0; i<neighbours.length; i++) {
                var n = neighbours[i];
                if(self.items[n].get("status") == "unblocked") {
                    self.items[n].set("status", "percolated");
                    percolateNeighboursRecursively(n);
                }
            }   
        }

        if(status === "percolated") {
            percolateNeighboursRecursively(position);
        }
        this.set("unblockedCount", this.get("unblockedCount") + 1);
        if(this.isConnected(this.top, this.bottom)) {
            this.set("percolated", true);
        }
    },
    
    isConnected: function(one, two) {
        return this.unionFind.find(one, two);
    },

    done: function() {
        return this.isConnected(this.top, this.bottom);
    },

    getNeighbours: function(position) {
        if(position < (this.top) || position > (this.bottom)) {
            throw new Error("Invalid Position " + String(position));
        }
        if(position === this.top) {
            return this._getVirtualTopNeighbours();
        }
        if(position === this.bottom) {
            return this._getVirtualBottomNeighbours();
        }

        neighbours = [];
        this._getAbove(position, neighbours).
             _getBelow(position, neighbours).
             _getLeft(position, neighbours).
             _getRight(position, neighbours);
        return neighbours;
    },
    _getVirtualTopNeighbours: function() {
        var arr = new Array(this.size);
        for(var i=0; i<arr.length; i++) {
            arr[i] = i + 1;
        }
        return arr;
    },
    _getVirtualBottomNeighbours: function() {
        var arr = new Array(this.size);
        for(var i=0; i<arr.length; i++) {
            arr[i] = this.bottom - i - 1;
        }
        return arr;
    },

    _getRow: function(position) {
        var value;
        if(position % self.size == 0) {
            value = (position / self.size) - 1
        }
        else {
            value = position / self.size;
        }
        return Math.floor(value);
    },
    
    _getColumn: function(position) {
        var value;
        if(position % self.size == 0) {
            value = self.size - 1
        }
        else {
            value = position % self.size - 1;
        }
        return Math.floor(value);
    },

    _getAbove: function(position, neighbours) {
        var value;
        if(this._getRow(position) == 0 ) {
            value = 0;
        }
        else {
            value = position - this.size;
        }
        neighbours.push(value);
        return this;
    },
    _getBelow: function(position, neighbours) {
        var value;
        if(this._getRow(position) == this.size - 1) {
            value = this.bottom
        }
        else {
            value = position + this.size;
        }
        neighbours.push(value);
        return this;
    },
    _getLeft: function(position, neighbours) {
        var value;
        if(this._getColumn(position) !== 0) {
            value = position - 1;
            neighbours.push(value);
        }
        return this;
    },
    _getRight: function(position) {
        var value;
        if(this._getColumn(position) !== (this.size - 1)) {
            value = position + 1;
            neighbours.push(value);
        }
        return this;
    }


});

var reset = function() {
    window.p.resetUnionFind().resetItems();
    window.tableView.reset();
}

var init = function() {
    size = 10;
    window.p = new Percolation({size: size});
    window.tableView = new TableView({size: size, model: window.p});
    window.tableView.render();
    
    $("#reset").click(function() {
        init();
        simulate();
    });
}


var simulate = function() {
    var times = 50;
    var n = 0;
    var i = 0;
    var j = 0;
    var results = new Array(times);
    var seen = {};

    var x = new Date();
    p.on("change:percolated", function() {
        if(p.attributes.percolated === true) {
            reset();
            results[n] = j / (size * size);
            $("#explored-count").html(j);
            j = 0;
            n += 1;
            var y = new Date();
            console.log("n: ", n, "Time taken for previous iteration: ", (y-x)/1000, " seconds");
            x = y;
            seen = {};
        }
    });

    var maxIters = 100000;
    var step = function() {
        if(n === times) {
            window.results = results;
            window.i = i;
            return;
        }
        if(i === maxIters) {
            console.error("Max iterations exceeded");
            return;
        }
        i += 1;
        j += 1;
        //console.info("j: ", j);
        
        var isSeen = true;
        var itemId;
        while(isSeen) {
            itemId = _.random(0, size*size-1);
            if(!seen[itemId]) {
                seen[itemId] = true;
                isSeen = false;
            }
        }
        tableView.items[itemId].updateUnionIds();
        window.requestAnimationFrame(step);
    }
    step();
}

$(document).ready(init)

